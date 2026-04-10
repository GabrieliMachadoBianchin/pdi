import cv2
import numpy as np

image = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
elemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(f"Elemento Estruturante (Kernel):\n{elemento}")
dilatacao = cv2.dilate(image, None)
dilatacao2 = cv2.dilate(image, elemento, iterations=3)
diferencaDilatacao = dilatacao - image
diferenca2dilatacao = dilatacao2 - dilatacao
cv2.imshow('Original', image)
cv2.imshow('Erosao 1', dilatacao)
cv2.imshow('Erosao 2', dilatacao2)
cv2.imshow('Diferenca Erosao', diferencaDilatacao)
cv2.imshow('Diferenca 2 Erosoes', diferenca2dilatacao)
cv2.waitKey(0)
cv2.destroyAllWindows()