import cv2 as cv
import numpy as np



blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

'''
# Colour RGB combination
blank[:]=0,255,0
'''

'''
# Colour RGB combination
blank[200:300,300:400]=0,255,255
'''


#2. Draw a rectangle
#                   coordinates
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)

# for full screen 
cv.rectangle(blank,(0,0),(500,500),(0,255,200),thickness=2)
cv.imshow('Rectangle',blank)

cv.waitKey(0)