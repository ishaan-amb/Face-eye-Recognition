import numpy as np              #for maths operations
import cv2
import time
count = 0           # starting from 0
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, 7)#cv2.COLOR_RGB2GRAY = 7 it has some code number
    cv2.imshow("my_image", gray)
    #cv2.imwrite("images/" + str(count) + "-image.jpg", img)                    #show only last image
    #count += 1
    #cv2.imshow(str(time.time()), img)               # no repeated time
    #time.sleep(1)
    cv2.waitKey(1)                                  # time interval

