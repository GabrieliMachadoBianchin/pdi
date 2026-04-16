import cv2
import numpy as np
import math
src = cv2.imread("aerion.jpg", cv2.IMREAD_GRAYSCALE)
dst = cv2.Canny(src, 50, 200, apertureSize=3)
cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
lines = cv2.HoughLines(dst, 1, np.pi / 180, 80)
if lines is not None:
    for i in range(len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1_x = int(round(x0 + 1000 * (-b)))
        pt1_y = int(round(y0 + 1000 * (a)))
        pt2_x = int(round(x0 - 1000 * (-b)))
        pt2_y = int(round(y0 - 1000 * (a)))
        cv2.line(cdst, (pt1_x, pt1_y), (pt2_x, pt2_y), (0, 0, 255), 3, cv2.LINE_AA)
else:
    print("Nenhuma linha foi detectada.")
cv2.imshow("Original (Grayscale)", src)
cv2.imshow("Detectado e Desenhado (Canny + Hough)", cdst)
cv2.waitKey(0)
cv2.destroyAllWindows()