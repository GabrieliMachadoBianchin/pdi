import cv2
import numpy as np

def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = frame[y, x]
        print(f"Cor no pixel ({x}, {y}): BGR {color}")

cap = cv2.VideoCapture(0)
cv2.namedWindow("Original")
cv2.setMouseCallback("Original", pick_color)

def nothing(x): pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Processamento")

cv2.createTrackbar("Baixa-Passa 1 (Blur)", "Processamento", 1, 30, nothing)
cv2.createTrackbar("Baixa-Passa 2 (Mediana)", "Processamento", 1, 30, nothing)

while True:
    ret, frame = cap.read()
    if not ret: break

    banda = frame[:, :, 1]

    k_blur = cv2.getTrackbarPos("Baixa-Passa 1 (Blur)", "Processamento") * 2 + 1
    k_med = cv2.getTrackbarPos("Baixa-Passa 2 (Median)", "Processamento") * 2 + 1

    img_filt = cv2.GaussianBlur(banda, (k_blur, k_blur), 0)
    img_filt = cv2.medianBlur(img_filt, k_med)

    laplacian = cv2.Laplacian(img_filt, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    _, binarizada = cv2.threshold(laplacian, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original", frame)
    cv2.imshow("Processamento", binarizada)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()