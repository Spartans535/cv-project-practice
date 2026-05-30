from ultralytics import YOLO
import cv2

def main():
    # 1. Initialize the lightweight Nano model engine
    # We choose 'nano' because it satisfies our strict real-time latency budget!
    model = YOLO("yolov8n.pt")

    # 2. Bind Python to your local hardware webcam stream
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream or webcam. Ensure camera permissions are active!")
        return

    print("Live YOLO Inference Pipeline Started!")
    print("Press the 'q' key while focusing the window to exit safely.")

    # 3. Enter the continuous frame processing loop
    while True:
        # A. Capture the current sequential frame matrix from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame from camera device.")
            break

        # B. Run full object detection inference on the frame in memory
        # verbose=False suppresses terminal log spam to optimize throughput speed
        results = model(frame, verbose=False)

        # C. Extract the first frame's data and plot the visual bounding boxes
        annotated_frame = results[0].plot()

        # D. Render the annotated frame matrix to your desktop window screen
        cv2.imshow("Live Real-Time YOLO Pipeline", annotated_frame)

        # E. Listen to the keyboard stream for 1 millisecond. If 'q' is pressed, break!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 4. Clean up systemic resource allocation handles
    cap.release()
    cv2.destroyAllWindows()
    print("Pipeline safely closed down.")

if __name__ == "__main__":
    main()