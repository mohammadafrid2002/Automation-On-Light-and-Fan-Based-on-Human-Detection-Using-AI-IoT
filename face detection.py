import cv2
import os
import serial

# Load the pre-trained Haar cascade for human detection
cascade_directory = r"D:\face detection"
cascade_filename = "haarcascade_frontalface_default.xml"
cascade_path = os.path.join(cascade_directory, cascade_filename)
face_cascade = cv2.CascadeClassifier(cascade_path)
# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initialize the serial connection to NodeMCU
arduino = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port
while True:
    # Capture video frame 
    ret, frame = cap.read()
    if ret:
        # Convert frame to grayscale for body detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      # Display the frame
        cv2.imshow('Face Detection', frame)
        # Check if face is detected
        if len(faces) > 0:
            print("Face detected")
            arduino.write(b'1')  # Send '1' command to turn on the LED
        else:
            print("No face detected")
            arduino.write(b'0')  # Send '0' command to turn off the LED

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
arduino.close()

