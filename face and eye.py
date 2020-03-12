import numpy as np              #for maths operations
import cv2
import time
count = 0           # starting from 0

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_detector = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret, img = cap.read()           #cv2.read("img.jpg")
    gray = cv2.cvtColor(img, 7)
    faces = face_detector.detectMultiScale(gray, 2,5)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 4)
        gray_face = gray[y:y+h, x:x+w]
        #gray_face = cv2.cvtColor(face, 7)
        eyes = eyes_detector.detectMultiScale(gray_face, 2, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (225, 0 , 0), 4)

    cv2.imshow("image", img)

    cv2.waitKey(1)