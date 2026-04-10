import cv2 as cv
import sys

img = cv.imread("ExTCC.jfif")

if img is None:
    sys.exit("Imagem não encontrada")

cv.namedWindow("Teste", cv.WINDOW_NORMAL)
cv.imshow("Teste", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("cap.png", img)