from ultralytics import YOLO
import os
import cv2

def main():
    # 1. Load the model brain
    model = YOLO("yolov8n.pt")
    
    image_path = os.path.join("src", "test.jpg")

    if not os.path.exists(image_path):
        print(f"Error: Cannot find {image_path}")
        return

    print("Running YOLO inference...")
    
    # 2. Run inference WITHOUT show=True. 
    # Instead, we just let the model calculate the boxes in memory.
    results = model(image_path)

    # 3. Extract the first result frame and plot the boxes onto a clean image array
    # .plot() draws the bounding boxes and text directly onto the pixel matrix
    annotated_image = results[0].plot()

    print("\nInference complete! Opening manual window wrapper...")
    
    # 4. Use standard OpenCV to show the annotated matrix frame
    cv2.imshow("YOLO Object Detection Result", annotated_image)

    # 5. This will now perfectly freeze the image window until you press a key!
    print("Press ANY key on your keyboard while focusing the image window to close it.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()