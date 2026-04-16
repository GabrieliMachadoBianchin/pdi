import cv2
import numpy as np
import random
original = cv2.imread("aerion.jpg")
original_with_rects = original.copy()
cinza = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
print("Detectando e preenchendo regiões...")
for y in range(cinza.shape[0]):
    for x in range(cinza.shape[1]):
        if cinza[y, x] == 255:
            fill_color = int(random.randint(0, 255))
            retval, cinza, mask, rect = cv2.floodFill(
                cinza,None, (x, y), fill_color,(0,), (0,),
                flags=cv2.FLOODFILL_FIXED_RANGE | 8)
            print(f"[{rect[0]},{rect[1]},{rect[2]},{rect[3]}]")
            cv2.rectangle(original_with_rects,(rect[0], rect[1]),
                   (rect[0] + rect[2], rect[1] + rect[3]),(0, 0, 255), 2,cv2.LINE_8, 0)
cv2.imshow("Imagem Original", original)
cv2.imshow("Imagem com Retângulos Detectados", original_with_rects)
cv2.imshow("Imagem Apos FloodFill (Regioes Preenchidas)", cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()