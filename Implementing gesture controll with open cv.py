import cv2
import numpy as np
import math
import sys
import traceback

# Try importing mediapipe and handle error if not installed
try:
    import mediapipe as mp
except ImportError:
    print("Error: 'mediapipe' library is required. Please install it using: pip install mediapipe")
    sys.exit(1)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Initialize Camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Controlled object initial properties
shape_center = [320, 240]  # Start at screen center (assuming 640x480)
shape_color = (0, 0, 255)  # Default: Red
shape_radius = 30          # Default radius

# Variables to track movement direction and history
prev_center = None
direction_text = "Stationary"
drawing_points = [] # For drawing lines when gesture is active

print("Program running. Press 'q' to quit.")

try:
    while True:
        ret, frame = cap.read()
        
        # 4. Error Handling: Failed frame capture
        if not ret:
            print("Error: Failed to capture image from camera.")
            break

        # Flip frame horizontally for a natural mirror effect
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        # Convert to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # 4. Error Handling / Fallback: Default status when no hand is detected
        hand_detected = False

        if results.multi_hand_landmarks:
            hand_detected = True
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on screen for visual debugging
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get key landmark coordinates (normalized to pixels)
                # Landmark 0: Wrist, 4: Thumb Tip, 8: Index Tip, 12: Middle Tip, 5: Index MCP
                landmarks = hand_landmarks.landmark
                
                # Use wrist or center of palm (Landmark 9) to track real-time position
                cx, cy = int(landmarks[9].x * w), int(landmarks[9].y * h)

                # --- 1. Extend Hand Tracking Functionality ---
                # Determine direction of movement (Up, Down, Left, Right)
                if prev_center is not None:
                    dx = cx - prev_center[0]
                    dy = cy - prev_center[1]
                    threshold = 8 # minimum pixel movement to trigger direction change
                    
                    if abs(dx) > abs(dy):
                        if dx > threshold: direction_text = "Right"
                        elif dx < -threshold: direction_text = "Left"
                    else:
                        if dy > threshold: direction_text = "Down"
                        elif dy < -threshold: direction_text = "Up"
                
                prev_center = (cx, cy)
                
                # Update controlled shape's center to follow the hand smoothly
                shape_center = [cx, cy]

                # --- 2. Add Additional Gestures ("Thumbs-up" or "Open hand") ---
                # Extract y-coordinates to check if fingers are open/extended
                # A finger is open if its tip y is lower than its pip/mcp joint y (in image coordinates, y decreases upward)
                index_open = landmarks[8].y < landmarks[6].y
                middle_open = landmarks[12].y < landmarks[10].y
                ring_open = landmarks[16].y < landmarks[14].y
                pinky_open = landmarks[20].y < landmarks[18].y
                
                # Check for Thumbs Up: horizontal thumb extension away from hand + other fingers closed
                # Assuming right hand mirror, thumb tip x < thumb mcp x, and other fingers curled
                thumb_is_up = (landmarks[4].y < landmarks[3].y) and not (index_open or middle_open or ring_open or pinky_open)
                open_hand = index_open and middle_open and ring_open and pinky_open

                if thumb_is_up:
                    gesture_text = "Thumbs Up!"
                    shape_color = (0, 255, 0) # Change shape color to Green
                    drawing_points.clear()    # Reset drawing lines
                elif open_hand:
                    gesture_text = "Open Hand"
                    shape_color = (255, 0, 0) # Change shape color to Blue
                    # Action: Draw a continuous line tracking the hand path
                    drawing_points.append((cx, cy))
                else:
                    gesture_text = "Tracking..."
                    shape_color = (0, 0, 255) # Revert to Red

                # --- 3. Create Dynamic Interaction (Distance scaling) ---
                # Calculate distance between Wrist (0) and Index Finger MCP (5) as a proxy for depth/distance from camera
                p0 = np.array([landmarks[0].x * w, landmarks[0].y * h])
                p5 = np.array([landmarks[5].x * w, landmarks[5].y * h])
                distance = math.hypot(p0[0] - p5[0], p0[1] - p5[1])
                
                # Dynamically adjust radius: Closer to camera = larger distance value = bigger shape
                shape_radius = int(np.clip(distance * 0.5, 15, 80))

                # Display gesture and direction data per frame
                cv2.putText(frame, f"Gesture: {gesture_text}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Movement: {direction_text}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        else:
            # 4. Error Handling: Hand lost/Not detected
            prev_center = None
            direction_text = "Stationary"
            cv2.putText(frame, "No hand detected / Poor lighting", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # --- Draw Actions on the screen ---
        # Draw trailing line if "Open Hand" was active
        if len(drawing_points) > 1:
            for i in range(1, len(drawing_points)):
                cv2.line(frame, drawing_points[i - 1], drawing_points[i], (255, 255, 0), 3)

        # Draw the dynamic tracking circle
        cv2.circle(frame, tuple(shape_center), shape_radius, shape_color, -1)
        
        # Display UI windows
        cv2.imshow('Interactive Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
