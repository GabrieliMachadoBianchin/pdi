import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray_image, 50, 100)
cv2.imshow("Original Image", image)
cv2.imshow("Canny ", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()