import cv2
import numpy as np
import random
def thresh_callback(thresh):
    canny_output = cv2.Canny(src_gray, thresh, thresh * 2, 3)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    print(f"{len(contours)} \nArea: ")
    for i in range(len(contours)):
        contour_area = cv2.contourArea(contours[i])
        print(f"<< {contour_area} << \"")
        color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        cv2.drawContours(drawing, contours, i, color, 2, cv2.LINE_8, hierarchy, 0, (0, 0))
    cv2.imshow("Contours", drawing)

src = cv2.imread("galinhas.png", 1)
src_gray = cv2.blur(src, (3, 3))
cv2.namedWindow("Source", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Source", src)
cv2.namedWindow("Contours", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Canny thresh:", "Source", 0, 255, thresh_callback)
thresh_callback(0)
cv2.waitKey(0)
cv2.destroyAllWindows()