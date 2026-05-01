import cv2

# precisa instalar a biblioteca contrib
# pip install opencv-contrib-python

video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo. Verifique o caminho!")
    exit()

trackers = []

success, frame = cap.read()

while True:
    bbox = cv2.selectROI("MultiTracker", frame, fromCenter=False, showCrosshair=True)

    tracker = cv2.TrackerCSRT.create()

    tracker.init(frame, bbox)
    trackers.append(tracker)

    print("Pressione 'S' para adicionar outro ou 'Enter' para iniciar.")
    k = cv2.waitKey(0) & 0xFF
    if k != ord('s'):
        break

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    for i, tracker in enumerate(trackers):
        ok, bbox = tracker.update(frame)

        if ok:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Objeto {i + 1}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            cv2.putText(frame, f"Objeto {i + 1} perdido", (10, 25 + (i * 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("MultiTracker", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc para sair
        break

cap.release()
cv2.destroyAllWindows()