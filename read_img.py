import cv2 as cv

img=cv.imread('Images/corgi2.jpg')   # selects image file
# Arranges and opens window according to size
cv.imshow('Dog',img)

#waits for infinite time for key to be pressed
cv.waitKey(0)