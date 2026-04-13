import cv2
import numpy as np

# Encontrar o retângulo vermelho, converter em grayscale, aplicar thresholding (preto/branco),
# utilizar erosão para diminuir a galinhas e separá-las, para enfim contá-las

img = cv2.imread('galinhas.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)

contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    roi = img[y:y + h, x:x + w]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((5, 5), np.uint8) # foi o melhor que eu consegui, contou 3 galinhas das 4
    eroded = cv2.erode(thresh, kernel, iterations=4)

    galinhas_contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Número de galinhas no retângulo: {len(galinhas_contours)}")

    cv2.imshow("ROI Binarizado e Erodido", eroded)
    cv2.waitKey(0)