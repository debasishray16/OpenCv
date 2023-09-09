import cv2 as cv

img=cv.imread('Images/corgi2.jpg')


def rescaleFrame(frame, scale=0.5):
    width= int(frame.shape[1] *scale)
    height= int(frame.shape[0]*scale)
    dimensions=(width,height)
    
    #interpolation = cv.INTER_AREA helps to downscale image because it helps to preserve the image quality.
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)





if img is None:
    print("Erro: Could not open or find the image.")

else:
    resize_image=rescaleFrame(img)
    cv.imshow('cat_dog', resize_image)
    cv.waitKey()
    cv.destroyAllWindows()


# This works only on live videos.
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)