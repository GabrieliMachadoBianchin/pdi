import cv2 as cv

src = cv.imread("../imagens/ExTCC.jfif")

if src is None:
    print("Não abre")
else:
    cv.namedWindow("Input", cv.WINDOW_NORMAL)
    cv.namedWindow("Output", cv.WINDOW_NORMAL)
    cv.imshow("Input", src)
    dst1 = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    cv.imshow("Output", dst1)
    cv.waitKey(0)
    cv.destroyAllWindows()