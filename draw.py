import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')

# 1. нарисовать blank одного цвета
blank[200:300, 300:400] = 0,0,255
cv.imshow('green', blank)

# 2. нарисовать квадрат
cv.rectangle(blank, (0,0), (blank.shape[0], blank.shape[0]), (0,255,0), thickness=-1)
cv.imshow('rectangle', blank)

# 3. нарисовать круг
cv.circle(blank, (blank.shape[0] // 2, blank.shape[0]// 2), 40, (0,255,0), thickness=-1)
cv.imshow('circle', blank)

# 4. нарисовать линию
print(blank.shape)
cv.line(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1], 0), (255,0,0), thickness=2)
cv.imshow('line', blank)

# 5. написать текст
cv.putText(blank, 'hello my name is egor', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,225,0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)