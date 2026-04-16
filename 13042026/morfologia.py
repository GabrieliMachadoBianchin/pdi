import cv2
import numpy as np

image = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
elemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(f"Elemento Estruturante (Kernel):\n{elemento}")
abertura = cv2.morphologyEx(image, cv2.MORPH_OPEN, elemento)
fechamento = cv2.morphologyEx(image, cv2.MORPH_CLOSE, elemento)
gradiente = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, elemento)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, elemento)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, elemento)
cv2.imshow('Original', image)
cv2.imshow('Abertura', abertura)
cv2.imshow('fechamento', fechamento)
cv2.imshow('gradiente', gradiente)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()