import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grad_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0,
                   ksize=3, scale=1, delta=0, borderType=cv2.BORDER_REPLICATE)
abs_grad_x = cv2.convertScaleAbs(grad_x)
grad_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1,
                   ksize=3, scale=1, delta=0, borderType=cv2.BORDER_REPLICATE)
abs_grad_y = cv2.convertScaleAbs(grad_y)
grad_final = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv2.imshow("Original Image", image)
cv2.imshow("Sobel(abs_grad_x + abs_grad_y)", grad_final)
cv2.waitKey(0)
cv2.destroyAllWindows()