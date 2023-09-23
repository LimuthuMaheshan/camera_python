import cv2

# Initialize the laptop's built-in camera (default camera, index 0)
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if  camera.isOpened():

    while True:
        ret, frame = camera.read()
        # Capture a frame from the camera



        if not ret:
            break 


        elif cv2.waitKey(1) & 0xFF==ord('q'):
            break

        # Display the captured frame

        # Exit the loop if 'q' is pressed
        else:
          cv2.imshow('Camera', frame)


else:
   
    print("Error: Could not open  camera.")
    exit()

# Release the camera
camera.release()
cv2.destroyAllWindows()
