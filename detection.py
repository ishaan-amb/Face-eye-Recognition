import numpy as np              #for maths operations
import cv2
import time
count = 0           # starting from 0

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, 7)
    faces = face_detector.detectMultiScale(gray, 2,5)

    if len(faces)>0:
        (x, y, w, h) = faces[0]

        face = img[y:y+h, x:x+w]


    # for(x, y, w, h) in faces:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (225, 0, 0), 4)

        cv2.imshow("image", face)

cv2.waitKey(1)