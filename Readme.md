# 🎯 Object Identification using Python (YOLOv8)

## 📌 Project Overview

This project is a real-time **Object Detection System** built using Python and the **YOLOv8 (You Only Look Once)** model.
It uses your webcam to detect and identify multiple objects instantly, draw bounding boxes, and display the number of detected objects.

---

## 🚀 Features

* 🔴 Real-time object detection using webcam
* ⚡ Fast and efficient detection using lightweight YOLOv8 model (`yolov8n`)
* 📦 Detects multiple objects simultaneously
* 🔢 Displays total object count in console
* 🖥️ Shows bounding boxes with labels

---

## 🛠️ Tech Stack

* Python 🐍
* OpenCV (cv2)
* Ultralytics YOLOv8

---

## 📂 Project Structure

```
object-identification-python/
│
├── main.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/object-identification-python.git
cd object-identification-python
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install ultralytics opencv-python
```

---

## ▶️ Usage

Run the Python script:

```
python main.py
```

* Webcam will open automatically
* Objects will be detected in real-time
* Press **Q** to exit

---

## 🧠 How It Works

1. Webcam captures live video frames
2. Each frame is passed to YOLOv8 model
3. Model detects objects and returns results
4. Bounding boxes are drawn on detected objects
5. Total object count is displayed

---

## 📸 Output

* Live video feed with detection
* Bounding boxes and labels
* Object count printed in terminal

---

## 💡 Future Improvements

* Add object tracking
* Save detection logs
* Add GUI interface
* Deploy as web app
* Use custom trained model

---

## 📜 Code Explanation (Main Logic)

```python
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Load pretrained model
cap = cv2.VideoCapture(0)   # Start webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  # Run detection

    count = len(results[0].boxes)  # Count objects
    print("Objects detected:", count)

    annotated_frame = results[0].plot()  # Draw boxes

    cv2.imshow("Smart Object Detector (Offline)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🙌 Acknowledgment

* YOLOv8 by Ultralytics
* OpenCV for image processing

---

## 👨‍💻 Author

**Deepesh Pandey**
MCA Student | Web Developer | AI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
