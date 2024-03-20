import cv2 as cv

img=cv.imread('image.jpg')
cv.imshow('Image',img)

def rescaleFrame(frame, scale=0.2):
    #Images Videos and LiveVideo
    
    width= int(frame.shape[1]* scale)
    height=int(frame.shape[0]*scale)
    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('ImageResized', resized_image)


def changeRes(width,height):
    #Live Videos
    capture.set(3,width)
    capture.set(4,height)
    



 #Reading Videos
capture=cv.VideoCapture('video.mp4')


while True:
    isTrue, frame=capture.read()

    frame_resized= rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)