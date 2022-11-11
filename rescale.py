import cv2 as cv

image = cv.imread('./Photos/cat.jpg')



def rescale_frame(frame, scale=0.75): # изменили размер видео на scale=0.75 => 75%
    """
    работает для Video, Images, Live Videos
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height): # изменяем разрешение видео
    """
    работает только для Live Video
    """
    capture.set(3, width)
    capture.set(4, height)


resized_image = rescale_frame(image)
cv.imshow('cat', resized_image)

capture = cv.VideoCapture('./Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('video resized', frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()