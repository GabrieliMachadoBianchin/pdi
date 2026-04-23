import cv2
import numpy as np
train_img = cv2.imread('aerion.jpg')
train_g = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
train_kp, train_desc = sift.detectAndCompute(train_g, None)
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann_matcher = cv2.FlannBasedMatcher(index_params, search_params)
if train_desc is not None and train_desc.shape[0] > 0:
    flann_matcher.add([train_desc])
else:
    print("Não foi possível adicionar descritores válidos de treinamento ao FLANN Matcher.")
cap = cv2.VideoCapture(0)
while True:
    ret, test = cap.read()
    test_g = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    test_kp, test_desc = sift.detectAndCompute(test_g, None)
    matches = []
    if test_desc is not None and test_desc.shape[0] > 0 and train_desc.shape[0] > 0:
        matches = flann_matcher.knnMatch(test_desc, k=2)
    else:
        pass
    good_matches = []
    for m, n in (match for match in matches if len(match) == 2):
        if m.distance < 0.6 * n.distance:
            good_matches.append(m)
    img_show = cv2.drawMatches( test, test_kp, train_img, train_kp, good_matches,
        None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow("Matches", img_show)
    key = cv2.waitKey(100) & 0xFF
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()