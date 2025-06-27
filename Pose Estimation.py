# Final Pose Estimation Project with Angle Tracking, Voice Feedback, and Snapshot Capture
import cv2
import time
import PoseModule as pm
import pyttsx3
import csv
import os

# Initialize camera
cap = cv2.VideoCapture(0)  # Use webcam
if not cap.isOpened():
    print("[ERROR] Cannot access camera.")
    exit()

# Initialize pose detector and text-to-speech
pTime = 0
spoken_90 = False
spoken_180 = False
spoken_wrong = False
engine = pyttsx3.init()
detector = pm.poseDetector()

# Create CSV file
log_file = "angle_log.csv"
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Angle"])

while True:
    success, img = cap.read()
    if not success or img is None:
        print("[INFO] Frame not captured.")
        break

    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=True)

    if len(lmList) != 0:
        # Right Arm: Shoulder(12), Elbow(14), Wrist(16)
        angle = detector.findAngle(img, 12, 14, 16)

        # Draw green dot on shoulder
        shoulder_x, shoulder_y = lmList[12][1], lmList[12][2]
        cv2.circle(img, (shoulder_x, shoulder_y), 10, (0, 255, 0), cv2.FILLED)

        # Provide audio feedback and snapshot for specific angles
        if 85 <= angle <= 95:
            if not spoken_90:
                engine.say("Perfect 90 degrees!")
                engine.runAndWait()
                spoken_90 = True
                spoken_180 = False
                spoken_wrong = False
                cv2.imwrite(f"snapshot_90_{int(time.time())}.jpg", img)
        elif 175 <= angle <= 185:
            if not spoken_180:
                engine.say("Perfect 180 degrees!")
                engine.runAndWait()
                spoken_180 = True
                spoken_90 = False
                spoken_wrong = False
                cv2.imwrite(f"snapshot_180_{int(time.time())}.jpg", img)
        else:
            if not spoken_wrong:
                engine.say("Wrong posture. Adjust your form.")
                engine.runAndWait()
                spoken_wrong = True
                spoken_90 = False
                spoken_180 = False

        # Log angle
        with open(log_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([time.time(), angle])

    # Show FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display window
    cv2.imshow("Pose Estimation Live", cv2.resize(img, (960, 720)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
