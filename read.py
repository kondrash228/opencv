import cv2 as cv


image = cv.imread('./Photos/cat_large.jpg')

cv.imshow('cat', image)

cv.waitKey(0)