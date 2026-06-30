import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    volume_available = True
except Exception as e:
    AudioUtilities = None
    IAudioEndpointVolume = None
    CLSCTX_ALL = None
    cast = None
    POINTER = None
    volume_available = False
    print(f"Volume API import error: {e}")

# Type hints for constants
if not volume_available:
    CLSCTX_ALL: int | None = None
    cast: callable | None = None
    POINTER: callable | None = None

Hands = mp.solutions.hands
hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

volctl = None
if volume_available:
    try:
        # Explicitly target the active multimedia audio output device
        from pycaw.constants import CLSCTX_ALL
        from comtypes import GUID
        
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volctl = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Quick test: Print current volume to console on startup to verify link
        current_vol = volctl.GetMasterVolumeLevelScalar()
        print(f"Successfully connected to Audio. Current Vol: {int(current_vol * 100)}%")
    except Exception as e:
        print(f"Pycaw initialization error: {e}")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible")
    exit()

WIN = "Hand Gesture Control"
cv2.namedWindow(WIN, cv2.WINDOW_NORMAL)

while True:
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)
    h, w = img.shape[:2]
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)

            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            ip = (int(lm[IX].x * w), int(lm[IX].y * h))

            cv2.circle(img, tp, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, ip, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, tp, ip, (0, 255, 0), 3)
            dist = float(np.hypot(ip[0] - tp[0], ip[1] - tp[1]))

            if label == "Left":  # real RIGHT hand -> volume (frame is flipped)
                v = np.interp(dist, [30, 300], [0.0, 1.0])
                if volctl is not None:
                    try:
                        volctl.SetMasterVolumeLevelScalar(float(v), None)
                    except Exception as e:
                        print(f"Volume error: {e}")

                bar = int(np.interp(dist, [30, 300], [400, 150]))
                pct = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(img, (50, bar), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            elif label == "Right":  # real LEFT hand -> brightness
                b = int(np.interp(dist, [30, 300], [0, 100]))
                try:
                    sbc.set_brightness(b)
                except Exception as e:
                    print(f"Brightness error: {e}")

                bar = int(np.interp(dist, [30, 300], [400, 150]))
                x1, x2 = w - 85, w - 50
                cv2.rectangle(img, (x1, 150), (x2, 400), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, bar), (x2, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f"{b}%", (w - 110, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow(WIN, img)
    key = cv2.waitKey(1)
    if key in (27, ord("q")):
        break

    try:
        if cv2.getWindowProperty(WIN, cv2.WND_PROP_VISIBLE) < 1:
            break
    except cv2.error:
        break

cap.release()
cv2.destroyAllWindows()
   