import cv2
import numpy as np
image_path = "aerion.jpg"
train = cv2.imread(image_path)
train_g = cv2.cvtColor(train, cv2.COLOR_BGR2GRAY)
hessian_threshold = 100
#devido a patentes na ultima versao do opencv foi descontinuado
surf = cv2.SURF_create(hessianThreshold=hessian_threshold))
train_kp, train_desc = surf.detectAndCompute(train_g, None)
print(f"Número de Keypoints SURF detectados: {len(train_kp)}")
if train_desc is not None:
    print(f"Shape dos descritores SURF: {train_desc.shape}")
else:
    print("Nenhum descritor SURF foi encontrado (provavelmente sem keypoints).")
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann_matcher = cv2.FlannBasedMatcher(index_params, search_params)
if train_desc is not None and train_desc.shape[0] > 0:
    flann_matcher.add([train_desc])
    print("Descritores adicionados ao FLANN Matcher.")
else:
    print("Nenhum descritor para adicionar ao FLANN Matcher.")
print("\nFLANN Matcher configurado e 'treinado' com os descritores da imagem de treinamento.")
print("Agora, 'flann_matcher' pode ser usado para encontrar correspondências.")
if train_kp and train_desc is not None:
    img_kp = cv2.drawKeypoints(train, train_kp, None, color=(0, 255, 0),
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("SURF Keypoints", img_kp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()