import numpy as np              #for maths operations
import cv2

#img = np.zeros((200, 400, 3), np.uint8)         #( width, hieght, depth )... Each pixel gives RGBA(Red, Green, Blue, Transparency)
img = cv2.imread("Screenshot(14).png")              #to display image

cv2.line(img, (100, 100), (200, 200), (255, 255, 255), 2)   # (start, ending point, colour, thickness)
cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 255), 2)

cv2.imshow("my_image", img)

cv2.waitKey(0)                                  # time interval
cv2.destroyAllWindows()
