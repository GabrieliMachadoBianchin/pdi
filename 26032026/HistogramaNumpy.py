import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread('ExTCC.jfif', cv.IMREAD_COLOR)
if src is None:
    print("Can't open image")
else:
    cv.imshow("Input", src)
    plt.hist(src.ravel(),256,[0,256]);
    plt.xlim([0, 256])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()