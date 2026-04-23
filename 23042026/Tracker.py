import cv2
import numpy as np

trackerKCF = cv2.TrackerKCF_create()
trackerCSRT = cv2.TrackerCSRT_create()
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture("d:/pdi/walking_commerce.mp4")
ok,frame=video.read()
bbox = cv2.selectROI(frame)
ok = trackerKCF.init(frame,bbox)
ok2 = trackerCSRT.init(frame,bbox)
while True:
   ok,frame=video.read()
   frame2 = frame.copy()
   ok,bbox=trackerKCF.update(frame)
   if ok:
        (x,y,w,h)=[int(v) for v in bbox]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2,1)
   else:
        cv2.putText(frame,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   ok2,bbox=trackerCSRT.update(frame2)
   if ok2:
        (x,y,w,h)=[int(v) for v in bbox]
        cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),2,1)
   else:
        cv2.putText(frame2,'Error',(100,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   cv2.namedWindow('Tracking KCF', cv2.WINDOW_GUI_NORMAL)
   cv2.namedWindow('Tracking CSRT', cv2.WINDOW_GUI_NORMAL)
   cv2.imshow('Tracking KCF',frame)
   cv2.imshow('Tracking CSRT',frame)
   if cv2.waitKey(1) & 0XFF==27:
        break
video.release()
cv2.destroyAllWindows()