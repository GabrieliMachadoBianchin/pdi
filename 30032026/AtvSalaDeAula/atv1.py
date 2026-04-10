import cv2 as cv
cap = cv.VideoCapture(0)

#cap = cv.VideoCapture('d:/pdi/race.mp4')
#cap = cv.VideoCapture('C:\Users\gabi\PycharmProjects\TestePDI\Semana4\AtvSalaDeAula')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # fazer o que quiser com o frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()