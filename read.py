import cv2 as cv

#img=cv.imread('image.jpg')

#cv.imshow('Image',img)

#Reading Videos

capture=cv.VideoCapture('video.mp4')
 
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)