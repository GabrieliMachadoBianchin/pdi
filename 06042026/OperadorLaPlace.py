import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.Laplacian(gray_image, cv2.CV_8U, ksize=3,
                    scale=1, delta=0, borderType=cv2.BORDER_REPLICATE)
laplace = cv2.convertScaleAbs(dst)
cv2.imshow("Original Image", image)
cv2.imshow("Laplace ", laplace)
cv2.waitKey(0)
cv2.destroyAllWindows()