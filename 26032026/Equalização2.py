import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('ExTCC.jfif', 0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.namedWindow("eq", cv.WINDOW_NORMAL)
cv.imshow("eq", res)
cv.waitKey(0)
cv.destroyAllWindows()