import cv2
import numpy as np
image = cv2.imread("aerion.jpg")
cv2.imshow("Imagem Original", image)
cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem em Escala de Cinza", cinza)
min_vals_bgr = np.array([200, 0, 0])
max_vals_bgr = np.array([255, 255, 255])
binariaNormal = cv2.inRange(image, min_vals_bgr, max_vals_bgr)
cv2.imshow("binariaNormal (inRange na BGR)", binariaNormal)
binaria = cv2.inRange(cinza, 100, 150)
cv2.imshow("binaria (inRange na Gray)", binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()