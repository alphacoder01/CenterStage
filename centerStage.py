import cv2
from PIL import Image
import numpy as np


camera = cv2.VideoCapture(1)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    _, frame = camera.read()
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    try:
        (x, y, nw, nh) = faces[0]

        new_width = 640
        new_height = 480

        y = y - nh//2
        x = x - nw//2

        img = frame[y:y + new_height, x:x + new_width]
        # img_final = cv2.resize(img, (640, 480), cv2.INTER_AREA)
        cv2.imshow('cropped', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        pass

camera.release()
cv2.destroyAllWindows()
