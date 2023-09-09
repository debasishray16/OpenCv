import numpy as np
import cv2 as cv
cap=cv.VideoCapture(0)

if not cap.isOpened():
    print("Error,: could not open the video capture.")
    exit()
    
else:
    new_width=1280
    new_height=720
    
    cap.set(3,new_width)
    cap.set(4,new_height)
    
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            break


cap.release()
cv.destroyAllWindows()