import cv2 as cv
from matplotlib import pyplot as plt
import os

def processar(img, cod_conversao, nomes_canais):
    #img_conv = cv.cvtColor(img, cod_conversao)
    #cv.imwrite("resultado_conversao.jpg", img_conv)

    #canais = cv.split(img_conv)
    canais = cv.split(img)
    for i, canal in enumerate(canais):
        nome = nomes_canais[i]

        cv.imshow(f"Canal {nome}", canal)
        cv.imwrite(f"canal_{nome}.jpg", canal)

        plt.figure()
        plt.title(f"Histograma - Canal {nome}")
        plt.hist(canal.ravel(), 256, [0, 256])
        plt.savefig(f"hist_canal_{nome}.png")
        plt.show()


def main():
    nome_arq = input("Digite o nome do diretório da imagem (com extensão): ")
    img = cv.imread(nome_arq)

    if img is None:
        print("Erro ao carregar imagem!")
        return

    opcoes = {
        '1': (cv.COLOR_BGR2RGB, ["R", "G", "B"]),
        '2': (cv.COLOR_BGR2HSV, ["H", "S", "V"]),
        '3': (cv.COLOR_BGR2XYZ, ["X", "Y", "Z"]),
        '4': (cv.COLOR_BGR2HLS, ["H", "L", "S"]),
        '5': (cv.COLOR_BGR2YCrCb, ["Y", "Cr", "Cb"]),
        '6': (cv.COLOR_BGR2Lab, ["L", "a", "b"]),
        '7': (cv.COLOR_BGR2Luv, ["L", "u", "v"])
    }

    num = 0
    while num != '8':
        print("\nEscolha um espaço de cor:")
        print("Escolha um espaço de cor:")
        print("1- RGB")
        print("2- HSV")
        print("3- XYZ")
        print("4- HLS")
        print("5- YCrCb")
        print("6- Lab")
        print("7- Luv")
        print("8- Sair")
        num = input("Opção: ")

        if num in opcoes:
            codigo, nomes = opcoes[num]
            processar(img, codigo, nomes)
            print(f"\nImagens e histogramas para a opção {num} salvos com sucesso!")
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif num == '8':
            print("Tchau!")
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()