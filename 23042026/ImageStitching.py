import cv2
import sys
#https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eye_cascade_name = cv2.data.haarcascades + 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier()
eye_cascade = cv2.CascadeClassifier()
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print(f"Erro: Não foi possível carregar o classificador de face '{face_cascade_name}'")
    sys.exit()
if not eye_cascade.load(cv2.samples.findFile(eye_cascade_name)):
    print(f"Aviso: Não foi possível carregar o classificador de olhos '{eye_cascade_name}'")
    eye_cascade = None
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if eye_cascade is not None:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1,
                minNeighbors=10, minSize=(15, 15) )
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('Face Detection (Haar Cascade)', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()