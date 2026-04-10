import cv2
import numpy as np

image = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
elemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(f"Elemento Estruturante (Kernel):\n{elemento}")
#dilatacao = cv2.dilate(image, None)
dilatacao = cv2.dilate(image, elemento, iterations=13)
diferencaDilatacao = dilatacao - image
#erosao = cv2.erode(dilatacao, None)
erosao = cv2.erode(dilatacao, elemento, iterations=13)
diferencaErosao = erosao - image
cv2.imshow('Original', image)
cv2.imshow('dilatacao', dilatacao)
cv2.imshow('Diferenca Dilatacao', diferencaDilatacao)
cv2.imshow('Erosao', erosao)
cv2.imshow('Diferenca Erosao', diferencaErosao)
cv2.waitKey(0)