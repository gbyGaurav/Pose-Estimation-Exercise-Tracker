

# 🧍‍♂️ Pose Estimation Exercise Tracker

This project uses **OpenCV**, **MediaPipe**, and **Python** to detect human poses in real-time via webcam. It calculates the angle between **shoulder**, **elbow**, and **wrist** joints to help users **track exercise posture**, **get audio feedback**, and **capture snapshots** when the pose is correct.

---

## 🔧 Features

* 🎥 Live video capture using webcam
* 📐 Calculates angle between shoulder–elbow–wrist
* ✅ Detects **perfect 90°** and **180°** angles
* 🔊 Provides **voice feedback** using `pyttsx3`
* 📸 Captures **snapshots** at perfect pose detection
* 📁 Logs all angles with timestamps in a CSV file
* ❌ Alerts on **wrong posture** using voice
* 🟢 Green dot shows tracked shoulder joint

---

## 📁 Project Structure

```bash
Pose-Estimation-Exercise-Tracker/
│
├── Pose Estimation.py          # Main script
├── PoseModule.py               # Custom module for pose detection and angle calculation
├── angle_log.csv               # Logged angles with timestamps
├── snapshot_90_*.jpg           # Snapshots at 90° (auto-generated)
├── snapshot_180_*.jpg          # Snapshots at 180° (auto-generated)
└── README.md                   # Project documentation
```

---

## 📦 Requirements

Install all required packages:

```bash
pip install opencv-python mediapipe pyttsx3
```

---

## ▶️ How to Run

Simply execute the main Python script:

```bash
python "Pose Estimation.py"
```

Make sure your webcam is connected.

---

## 📊 Use Case

This project is especially useful for:

* Fitness and gym trainers
* Home workout posture correction
* Rehabilitation and physical therapy tracking
* AI-based exercise form feedback systems

---

## 🤖 Built With

* Python 🐍
* OpenCV 📷
* MediaPipe 🖐️
* pyttsx3 🔊

---

## 🏁 Future Improvements

* Count reps automatically
* Add support for different types of exercises
* Upload data to a cloud-based dashboard
* Use ML model to classify correct vs. incorrect forms

---

📢 Author
Gaurav Deore

For any queries or collaboration, feel free to contact.
