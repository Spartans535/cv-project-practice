import cv2
import os

def main():
    # This explicitly points OpenCV to look inside the src folder
    image_path = os.path.join("src", "test.jpg")
    
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Still can't find the image at {image_path}")
        return

    print(f"Success! Image Shape: {img.shape}")
    cv2.imshow("OpenCV Test Window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()