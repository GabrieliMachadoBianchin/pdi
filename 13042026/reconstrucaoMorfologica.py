import cv2
import numpy as np
def imreconstruct(marker: np.ndarray, mask: np.ndarray, radius: int = 1):
    kernel = np.ones(shape=(radius * 2 + 1,) * 2, dtype=np.uint8)
    while True:
        expanded = cv2.dilate(src=marker, kernel=kernel)
        cv2.bitwise_and(src1=expanded, src2=mask, dst=expanded)
        if (marker == expanded).all():
            return expanded
        marker = expanded

image = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
image = 255 - image
elemento = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(f"Elemento Estruturante (Kernel):\n{elemento}")
erosao = cv2.erode(image, elemento, iterations=9)
reconstruida = imreconstruct(erosao, image)
cv2.imshow('Original', image)
cv2.imshow('erosao', erosao)
cv2.imshow('reconstruida', reconstruida)
cv2.waitKey(0)
cv2.destroyAllWindows()