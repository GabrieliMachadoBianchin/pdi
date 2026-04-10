import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('Aerion.jfif', 0)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
equ = cv.equalizeHist(img)
res = np.hstack((img, cl1, equ))
cv.namedWindow("eq", cv.WINDOW_NORMAL)
cv.imshow("eq", res)
cv.waitKey(0)
cv.destroyAllWindows()