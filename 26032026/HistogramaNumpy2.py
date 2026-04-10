import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread('ExTCC.jfif', cv.IMREAD_COLOR)
if src is None:
    print("Can't open image")
else:
    cv.imshow("Input", src)
    src = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    mask = np.zeros(src.shape[:2], np.uint8)
    mask[150:1000, 150:1000] = 255
    masked_img = cv.bitwise_and(src, src, mask=mask)
    # Calculate histogram with mask and without mask
    # Check third argument for mask
    hist_full = cv.calcHist([src], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([src], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(src, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()