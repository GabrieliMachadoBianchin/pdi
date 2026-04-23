import cv2 as cv

src = cv.imread("../imagens/ExTCC.jfif", cv.IMREAD_COLOR)

if src is None:
    print("Não abre")
else:
    cv.namedWindow("Input", cv.WINDOW_NORMAL)
    cv.imshow("Input", src)
    b, g, r = cv.split(src)
    cv.namedWindow("B", cv.WINDOW_NORMAL)
    cv.imshow("B", b)
    cv.namedWindow("G", cv.WINDOW_NORMAL)
    cv.imshow("G", g)
    cv.namedWindow("R", cv.WINDOW_NORMAL)
    cv.imshow("R", r)
    cv.waitKey(0)
    cv.destroyAllWindows()