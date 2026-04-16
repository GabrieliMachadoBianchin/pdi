import cv2
import numpy as np
img = cv2.imread("aerion.jpg")
orig = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, gray_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
elemento = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
gray_morphed = cv2.morphologyEx(gray_thresh, cv2.MORPH_OPEN, elemento, iterations=7)
borda = cv2.Canny(gray_morphed, 25, 100, apertureSize=3)
circles = cv2.HoughCircles(borda, cv2.HOUGH_GRADIENT, 2, gray.shape[0] / 4,
                           param1=200, param2=100, minRadius=0, maxRadius=0)
if circles is not None:
    circles = np.uint16(np.round(circles[0, :]))
    for i in circles:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(orig, center, 3, (0, 255, 0), -1, 8, 0)
        cv2.circle(orig, center, radius, (0, 0, 255), 3, 8, 0)
        print(f"Círculo detectado: Centro=({center[0]}, {center[1]}), Raio={radius}")
else:
    print("Nenhum círculo foi detectado.")
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Thresholded (Otsu) Image", gray_thresh)
cv2.imshow("Morphed Image (Opening)", gray_morphed)
cv2.imshow("Canny Edges", borda)
cv2.imshow("Detected Circles", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()