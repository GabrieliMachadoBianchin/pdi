import cv2
import numpy as np

image = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
elemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(f"Elemento Estruturante (Kernel):\n{elemento}")
erosao = cv2.erode(image, None)
erosao2 = cv2.erode(image, elemento, iterations=3)
diferencaErosao = image - erosao
diferenca2Erosoes = erosao - erosao2
cv2.imshow('Original', image)
cv2.imshow('Erosao 1', erosao)
cv2.imshow('Erosao 2', erosao2)
cv2.imshow('Diferenca Erosao', diferencaErosao)
cv2.imshow('Diferenca 2 Erosoes', diferenca2Erosoes)
cv2.waitKey(0)
cv2.destroyAllWindows()