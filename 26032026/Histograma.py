import cv2 as cv
from matplotlib import pyplot as plt

src = cv.imread('ExTCC.jfif', cv.IMREAD_COLOR)
if src is None:
    print("Can't open image")
else:
    cv.imshow("Input", src)
    histB = cv.calcHist([src],[0],None,[256],[0,256])
    plt.plot(histB, color='b')
    plt.xlim([0, 256])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()
