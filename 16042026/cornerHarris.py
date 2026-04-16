import cv2
import numpy as np
original = cv2.imread("aerion.jpg")
cinza = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Original (BGR)", original)
cv2.imshow("Imagem em Escala de Cinza", cinza)
block_size = 2
size_sobel_kernel = 3
k = 0.1
corners = cv2.cornerHarris(cinza, block_size, size_sobel_kernel, k, borderType=cv2.BORDER_DEFAULT)
corners_normalized = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX)
corners_processed = cv2.convertScaleAbs(corners_normalized)
corners_on_original = original.copy()
threshold_value = 150
strong_corners_y, strong_corners_x = np.where(corners_processed > threshold_value)
for x, y in zip(strong_corners_x, strong_corners_y):
    cv2.circle(corners_on_original, (x, y), 3, (0, 0, 255), -1)
cv2.imshow("Harris Corner Response (Processed)", corners_processed)
cv2.imshow("Corners Detected on Original Image", corners_on_original)
cv2.waitKey(0)
cv2.destroyAllWindows()