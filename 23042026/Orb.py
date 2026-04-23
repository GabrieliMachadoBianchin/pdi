import cv2
import numpy as np
image_path = "aerion.jpg"
train_img_color = cv2.imread(image_path)
train_img_gray = cv2.cvtColor(train_img_color, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(nfeatures=500)
train_kp, train_desc = orb.detectAndCompute(train_img_gray, None)
bf_matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
cap = cv2.VideoCapture(0)
while True:
    ret, current_frame_color = cap.read()
    current_frame_gray = cv2.cvtColor(current_frame_color, cv2.COLOR_BGR2GRAY)
    current_kp, current_desc = orb.detectAndCompute(current_frame_gray, None)
    matches = []
    if current_desc is not None and current_desc.shape[0] > 0:
        matches = bf_matcher.match(current_desc)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = matches
    else:
        good_matches = []
    output_img = cv2.drawMatches(current_frame_color, current_kp, train_img_color, train_kp,
        good_matches,None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.putText(output_img, f"Matches: {len(good_matches)}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("ORB Live Matching", output_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()