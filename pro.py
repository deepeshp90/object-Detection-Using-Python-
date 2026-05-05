from ultralytics import YOLO
import cv2

# Use lightweight model (must already be downloaded once)
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Count objects
    count = len(results[0].boxes)
    print("Objects detected:", count)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("Smart Object Detector (Offline)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()