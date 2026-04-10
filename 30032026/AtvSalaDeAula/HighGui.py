import cv2 as cv
import numpy as np
def funcao(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"Botao esquerdo apertado ({x}, {y})")
    elif event == cv.EVENT_RBUTTONDOWN:
        print(f"Botao direito apertado ({x}, {y})")
    elif event == cv.EVENT_MBUTTONDOWN:
        print(f"Botao meio apertado ({x}, {y})")
    elif event == cv.EVENT_MOUSEMOVE:
        print(f"movimento mouse apertado ({x}, {y})")

img = cv.imread('ExTCC.jfif')
cv.namedWindow('teste')
cv.setMouseCallback('teste', funcao)
cv.imshow('teste', img)
cv.waitKey(0)
cv.destroyAllWindows()