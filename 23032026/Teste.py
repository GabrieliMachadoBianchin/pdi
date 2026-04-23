import cv2  # Biblioteca OpenCV
import sys  # Para tratamento de erros

def main():
    # Caminho da imagem (altere para o caminho da sua imagem)
    image_path = "../imagens/ExTCC.jfif"

    # Tenta carregar a imagem
    image = cv2.imread(image_path)

    # Verifica se a imagem foi carregada corretamente
    if image is None:
        print(f"Erro: não foi possível carregar a imagem '{image_path}'.")
        sys.exit(1)

    # Exibe a imagem original
    cv2.imshow("Imagem Original", image)

    # Converte para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Exibe a imagem em escala de cinza
    cv2.imshow("Imagem em Escala de Cinza", gray_image)

    # Salva a imagem em escala de cinza
    output_path = "saida_cinza.jpg"
    cv2.imwrite(output_path, gray_image)
    print(f"Imagem em escala de cinza salva como '{output_path}'.")

    # Aguarda até que uma tecla seja pressionada
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
