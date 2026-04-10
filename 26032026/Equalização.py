import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('ExTCC.jfif', 0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.subplot(131), plt.imshow(img, 'gray')
plt.subplot(132), plt.plot(cdf_normalized, color = 'b')
plt.subplot(132), plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.subplot(132), plt.xlim([0,256]), plt.legend(('cdf','histogram'), loc = 'upper left')
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]
plt.subplot(133), plt.imshow(img2, 'gray')
plt.show()