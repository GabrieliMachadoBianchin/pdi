import cv2
import numpy as np

def on_trackbar_change(val):
    max_corners = max(1, val)
    quality = 0.01
    min_distance = 10
    corners = cv2.goodFeaturesToTrack(
        image_gray, maxCorners=max_corners,
        qualityLevel=quality, minDistance=min_distance)
    image_corners = image.copy()
    if corners is not None:
        for i in range(corners.shape[0]):
            x, y = corners[i, 0]
            cv2.circle(image_corners, (int(x), int(y)), 4, (0, 0, 255), -1)
    cv2.imshow("Corners", image_corners)

# image = cv2.imread(r"C:\Users\utfpr\PycharmProjects\pdi\pdi\imagens\aerion.jpg")
image = cv2.imread(r"aerion.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Corners")
max_corners = 100
cv2.createTrackbar("Max no. of corners", "Corners",
        max_corners, 500, on_trackbar_change)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
cv2.destroyAllWindows()