import cv2 as cv
import numpy as np


image = cv.imread('./Photos/park.jpg')
cv.imshow('park', image)

# translation
def translate(image, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (image.shape[1], image.shape[0])

    return cv.warpAffine(image, transMat, dimensions)

"""
-x --> left
-y --> up
x --> right
y --> down
"""

translated = translate(image, -100, 100)
cv.imshow('translated', translated)


# rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(image, -45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('rotated_rotated', rotated_rotated)

# resize
resized = cv.resize(image, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flipping
flip = cv.flip(image, 0)
cv.imshow('flip', flip)
 
# cropping 2
cropped = image[200:400, 300:400]
cv.imshow('cropped 2', cropped)
  
cv.waitKey(0)