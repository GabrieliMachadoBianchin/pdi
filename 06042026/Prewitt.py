import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
filtro = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [-1, -1, -1]])
sai = cv2.filter2D(gray_image, -1, filtro)
cv2.imshow("Original Image", image)
cv2.imshow("Filtro", sai)
cv2.waitKey(0)
cv2.destroyAllWindows()