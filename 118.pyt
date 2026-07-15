import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
import time
import mediapipe as mp
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# Configuration
SCROLL_SPEED = 300
SCROLL_DELAY = 3  # Give it a small buffer so it doesn't fly off the screen instantly
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    
    # 4 Fingers: Index, Middle, Ring, Pinky
    tips = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    
    for tip in tips:
        # If tip is higher (lower Y value) than PIP joint, finger is UP
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
            
    # Thumb logic
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    else:
        fingers.append(0)

    # Return action state
    total_up = sum(fingers)
    if total_up == 5:
        return "scroll_up"
    elif total_up == 0:
        return "scroll_down"
    return "none"

# Setup Video Capture
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

last_scroll = 0
p_time = 0 

print("Gesture based scroller active...")
print("Open Palm = Scroll Up | Closed Fist = Scroll Down | Press 'q' to Quit")

while cap.isOpened():
    success, img = cap.read()
    if not success: 
        break
    
    # Mirror image
    img = cv2.flip(img, 1)
    
    # MediaPipe needs RGB, but OpenCV needs BGR to display correctly later
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    gesture = "none"
    handedness = "Unknown"
    
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand, handedness)
            
            # Draw visual tracking lines onto the original frame
            mp_drawing.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
            
            # Handle PyAutoGUI actions
            current_time = time.time()
            if current_time - last_scroll > SCROLL_DELAY:
                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)
                    last_scroll = current_time
                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)
                    last_scroll = current_time

    # FPS Calculation
    c_time = time.time()
    fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0
    p_time = c_time
    
    # UI Overlay
    cv2.putText(img, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f"FPS: {int(fps)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Hand Gesture Scroll Control", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()