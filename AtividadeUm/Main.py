import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def main():
    nome_arquivo = input("Digite o nome da imagem: ")
    src = cv.imread(nome_arquivo)

    if src is None:
        print("Erro ao carregar a imagem.")
        return

    num = 0
    while num != '8':
        print("\nEscolha um espaço de cor:")
        print("1- RGB")
        print("2- HSV")
        print("3- XYZ")
        print("4- HLS")
        print("5- YCrCb")
        print("6- Lab")
        print("7- Luv")
        print("8- Sair")
        num = input("Opção: ")

        dst = None
        canais_nomes = []

        if num == '1':
            dst = cv.cvtColor(src, cv.COLOR_BGR2RGB)
            canais_nomes = ['R', 'G', 'B']
        elif num == '2':
            dst = cv.cvtColor(src, cv.COLOR_BGR2HSV)
            canais_nomes = ['H', 'S', 'V']
        elif num == '3':
            dst = cv.cvtColor(src, cv.COLOR_BGR2XYZ)
            canais_nomes = ['X', 'Y', 'Z']
        elif num == '4':
            dst = cv.cvtColor(src, cv.COLOR_BGR2HLS)
            canais_nomes = ['H', 'L', 'S']
        elif num == '5':
            dst = cv.cvtColor(src, cv.COLOR_BGR2YCrCb)
            canais_nomes = ['Y', 'Cr', 'Cb']
        elif num == '6':
            dst = cv.cvtColor(src, cv.COLOR_BGR2Lab)
            canais_nomes = ['L', 'a', 'b']
        elif num == '7':
            dst = cv.cvtColor(src, cv.COLOR_BGR2Luv)
            canais_nomes = ['L', 'u', 'v']
        elif num == '8':
            print("Tchau!")
            break
        else:
            print("Opção inválida!")
            continue

        if dst is not None:
            cv.imwrite(f"resultado_opcao_{num}.jpg", dst)
            cv.imshow(f"{num}", dst)
            canais = cv.split(dst)

            for i in range(len(canais)):
                nome = canais_nomes[i]
                imagem_canal = canais[i]

                cv.imshow(f"Canal {nome} - Opcao {num}", imagem_canal)

                cv.imwrite(f"opcao_{num}_canal_{nome}.jpg", imagem_canal)

                plt.figure()
                plt.title(f"Histograma Canal {nome} (Opção {num})")
                plt.xlabel("Intensidade")
                plt.ylabel("Qtd de Pixels")
                # calcHist([imagem], [canal], mascara, [bins], [intervalo])
                hist = cv.calcHist([imagem_canal], [0], None, [256], [0, 256])
                plt.plot(hist)
                plt.xlim([0, 256])
                plt.savefig(f"hist_opcao_{num}_canal_{nome}.png")
                plt.show()

            print(f"Processamento da opção {num} concluído e arquivos salvos.")
            cv.waitKey(0)
            cv.destroyAllWindows()


if __name__ == "__main__":
    main()