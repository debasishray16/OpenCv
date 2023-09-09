import cv2 as cv2


vid = cv.VideoCapture(0)
# 0 = My computer Camera
# 1 = for another camera

#readind frames one by one.
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    
    if (cv.waitKey(20) & 0xFF==ord('d')):
        break
    
capture.release()

cv.destroyAllWindows()