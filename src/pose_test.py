from ultralytics import YOLO
import os
import cv2

def main():
    # 1. Load the pre-trained YOLOv8 'Nano' POSE model
    # The '-pose' version is specifically trained to map 17 human skeletal joints!
    model = YOLO("yolov8n-pose.pt")

    image_path = os.path.join("src", "test.jpg")

    if not os.path.exists(image_path):
        print(f"Error: Cannot find {image_path}")
        return

    print("Running YOLO Keypoint Pose Estimation...")
    
    # 2. Process the image through the pose neural network
    results = model(image_path)

    # 3. Use the built-in renderer to overlay the skeletal bones and joint dots
    annotated_image = results[0].plot()

    print("\nInference complete! Rendering skeletal grid...")
    
    # 4. Use standard OpenCV to show the annotated matrix frame safely
    cv2.imshow("YOLO Pose Keypoint Estimation", annotated_image)

    # 5. Perfect freeze wrapper
    print("Press ANY key on your keyboard while focusing the image window to close it.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()