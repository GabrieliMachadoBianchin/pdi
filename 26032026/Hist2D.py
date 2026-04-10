import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Aerion.jfif', cv.IMREAD_COLOR)
cv.imshow("Input", img)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
hist = cv.calcHist([hsv], [0, 1], None, [256, 256], [0, 256, 0, 256])
plt.imshow(hist,interpolation = 'nearest')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()