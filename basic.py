import cv2 as cv

image = cv.imread('./Photos/park.jpg')
cv.imshow('park', image)


# преобразование изображения в оттенки серого
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# размытие фото (blur)
blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# нахождение краев (edge cascade)
cany = cv.Canny(blur, 125, 125)
cv.imshow('cany', cany)

# расширение фото (dilating)
dilated = cv.dilate(cany, (7,7), iterations=3)
cv.imshow('dilated', dilated)

# разрушение (eroding)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', eroded) 

# размер фото (resize)
resized = cv.resize(image, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropping
cropped = image[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)