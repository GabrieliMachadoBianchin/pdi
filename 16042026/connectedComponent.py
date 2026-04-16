import cv2
import numpy as np

# img_original = np.zeros((300, 400), dtype=np.uint8)
# cv2.circle(img_original, (100, 100), 30, 255, -1)
# cv2.rectangle(img_original, (200, 50), (280, 150), 255, -1)
# cv2.ellipse(img_original, (100, 250), (60, 30), 45, 0, 360, 255, -1)
# cv2.circle(img_original, (350, 200), 15, 255, -1)
# cv2.circle(img_original, (365, 215), 15, 255, -1)

img_original = cv2.imread("galinhas.png")
binary_img = img_original.copy()
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    binary_img, connectivity=8, ltype=cv2.CV_32S
)
print(f"Número de componentes conectados (incluindo o fundo): {num_labels}")
output_img_colored = cv2.cvtColor(binary_img, cv2.COLOR_GRAY2BGR)
for i in range(1, num_labels):
    x = stats[i, cv2.CC_STAT_LEFT]    # Coordenada X mais à esquerda da caixa delimitadora
    y = stats[i, cv2.CC_STAT_TOP]     # Coordenada Y mais ao topo da caixa delimitadora
    w = stats[i, cv2.CC_STAT_WIDTH]   # Largura da caixa delimitadora
    h = stats[i, cv2.CC_STAT_HEIGHT]  # Altura da caixa delimitadora
    area = stats[i, cv2.CC_STAT_AREA] # Área (número de pixels) do componente
    (cX, cY) = centroids[i]
    if area < 50:
        continue
    cv2.rectangle(output_img_colored, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.circle(output_img_colored, (int(cX), int(cY)), 4, (0, 0, 255), -1)
    cv2.putText(output_img_colored, f"ID: {i}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
    cv2.putText(output_img_colored, f"Area: {area}", (x, y + h + 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)

    print(f"Componente {i}: X={x}, Y={y}, Largura={w}, Altura={h}, Área={area}, "
          f"Centroide=({cX:.2f}, {cY:.2f})")
cv2.imshow("1. Imagem Original (Binaria)", binary_img)
cv2.imshow("2. Componentes Conectados (Com Stats)", output_img_colored)
cv2.waitKey(0)
cv2.destroyAllWindows()