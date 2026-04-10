import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filtro1 = np.array([[1, 0],
                   [0, -1],])
filtro2 = np.array([[-1, 0],
                   [0, 1],])
filtro3 = np.array([[0, 1],
                   [-1, 0],])
filtro4 = np.array([[0, -1],
                   [1, 0],])

sai1 = cv2.filter2D(gray_image, -1, filtro1)
sai2 = cv2.filter2D(gray_image, -1, filtro2)
sai3 = cv2.filter2D(gray_image, -1, filtro3)
sai4 = cv2.filter2D(gray_image, -1, filtro4)

sai = sai1 + sai2 + sai3 + sai4

cv2.imshow("Original Image", image)
cv2.imshow("Filtro", sai)
cv2.waitKey(0)
cv2.destroyAllWindows()