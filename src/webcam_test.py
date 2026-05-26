import cv2

def main():
    # 0 opens the default built-in webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam activated successfully! Press 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Display the resulting live video frame in a window
        cv2.imshow('Live Webcam Feed', frame)

        # Break the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and close windows when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()