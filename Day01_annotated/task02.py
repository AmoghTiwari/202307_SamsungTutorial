"References: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html"

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open camera. Exitting ...")
    exit()

count=0
while True:
    count+= 1
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exitting ...")
        break

    cv2.imshow('frame', frame) # Display the frame

    cv2.imwrite(f"../data/01_IO/vid_frames/{count:04d}.jpg", frame)

    if cv2.waitKey(1) == ord('q'):
        # waitKey -> Allows to display a window for 'x' miliseconds or till a key is pressed
        break

cap.release()
cv2.destroyAllWindows()
