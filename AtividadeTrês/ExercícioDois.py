import cv2
import numpy as np

# Blur para suavizar o chão, Canny para detectar bordas, dilatação para preeencher as bolas
# thresholding, desenhar contornos

img = cv2.imread('bolinhas.png')

## Tentativa 1 com grayscale
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blurred = cv2.medianBlur(gray, 7)
#edges = cv2.Canny(blurred, 50, 150)
#kernel = np.ones((3,3), np.uint8)
#dilated_edges = cv2.dilate(edges, kernel, iterations=1)
#contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#binary_result = np.zeros_like(gray)
#cv2.drawContours(binary_result, contours, -1, (255), thickness=-1)

## Tentativa 2 com HSV e saturação
# e fechamento + dilatação
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h = Hue (Cor), s = Saturation (Saturação), v = Value (Brilho)
h, s, v = cv2.split(hsv)
blurred = cv2.medianBlur(s, 7)
edges = cv2.Canny(blurred, 4, 50)
kernel = np.ones((6,6), np.uint8)
closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

binary_result = np.zeros_like(s)
cv2.drawContours(binary_result, contours, -1, 255, thickness=-1)

cv2.imshow("1. Bordas (Canny)", edges)
cv2.imshow("2. Imagem Binaria Final", binary_result)
cv2.waitKey(0)
cv2.destroyAllWindows()