import cv2 as cv

img=cv.imread('image.jpg')

cv.imshow('Image',img)

cv.waitKey(0)