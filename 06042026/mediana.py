import cv2
import numpy as np
def update_mediana(tamBloco):
    dst = cv2.medianBlur(src, 1+tamBloco*2)
    cv2.imshow("testaBlur", dst)

src = cv2.imread("aerion.jpg")
cv2.namedWindow("testaBlur", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Tamanho Bloco:", "testaBlur", 0, 50, update_mediana)
update_mediana(0)
while True:
    c = cv2.waitKey(20) & 0xFF
    if c == 27:
       break
cv2.destroyAllWindows()