"""
25) Faça um programa  para determnar a próxima jogada em um Jogo da Velha.
Assumir que o tabuleiro é representado por uma matriz de 3 x 3, onde cada
posição representa uma das casas do tabuleiro. A matriz pode conter os
seguintes valores -1, 0, 1 representando respectivamente uma casa contendo uma
peça minha (-1), uma casa vazia do tabuleiro (0), e uma casa contendo uma peça
do seu oponente (1)

Exemplo:

    x  |  o  |  x
    o  |  o  |  o
    o  |  o  |  o

OBS: PREFERI FAZER UM JOGO DA VELHA COMPLETO
"""

jogo = []

for i in range(3):

    velha = []
    for j in range(3):
        velha.append('-')

    jogo.append(velha)

cont = 1
vezes = 0

# Indicador se o jogo continua ou não
continua = True

while continua:

    # Imprimir como o jogo está antes de cada jogada
    for i in range(3):

        for j in range(3):
            print(jogo[i][j], end='  ')

        print()

    if cont % 2 == 0:
        print("\nVez do jogador 'x'")

    elif cont % 2 == 1:
        print("\nVez do jogador 'o'")

    linha = int(input("Digite a linha que você deseja colocar a peça (1 à 3): "))
    if (linha >= 1) and (linha <= 3):
        coluna = int(input("Digite a coluna que você deseja colocar a peça (1 à 3): "))

        if (coluna >= 1) and (coluna <= 3):

            if cont % 2 == 0:

                if jogo[linha-1][coluna-1] == '-':
                    jogo[linha-1][coluna-1] = 'x'

                    vezes += 1

                else:
                    print("Perdeu a vez: existe uma peça nesse local\n")

            elif cont % 2 == 1:
                if jogo[linha-1][coluna-1] == '-':
                    jogo[linha-1][coluna-1] = 'o'

                    vezes += 1

                else:
                    print("Perdeu a vez: existe uma peça nesse local\n")

        else:
            print("Perdeu a vez: coluna inválida\n")
            cont += 1
            continue

    else:
        print("Perdeu a vez: linha inválida\n")
        cont += 1
        continue

    for i in range(-1, 2, 1):

        if (i == -1) or (i == 1):

            for j in range(3):

                if i == -1:

                    # Caso dê velha na horizontal
                    if jogo[j][0] == 'x' and jogo[j][1] == 'x' and jogo[j][2] == 'x':
                        print("\nO jogador 'x' venceu")
                        continua = False
                        break

                    # Caso dê velha na vertical
                    elif jogo[0][j] == 'x' and jogo[1][j] == 'x' and jogo[2][j] == 'x':
                        print("\nO jogador 'x' venceu")
                        continua = False
                        break

                    # Caso dê velha na diagonal principal
                    elif jogo[0][0] == 'x' and jogo[1][1] == 'x' and jogo[2][2] == 'x':
                        print("\nO jogador 'x' venceu")
                        continua = False
                        break

                    # Caso dê velha na diagonal inversa
                    elif jogo[0][2] == 'x' and jogo[1][1] == 'x' and jogo[2][0] == 'x':
                        print("\nO jogador 'x' venceu")
                        continua = False
                        break

                if i == 1:
                    # Caso dê velha na horizontal
                    if jogo[j][0] == 'o' and jogo[j][1] == 'o' and jogo[j][2] == 'o':
                        print("\nO jogador 'o' venceu")
                        continua = False
                        break

                    # Caso dê velha na vertical
                    elif jogo[0][j] == 'o' and jogo[1][j] == 'o' and jogo[2][j] == 'o':
                        print("\nO jogador 'o' venceu")
                        continua = False
                        break

                    # Caso dê velha na diagonal principal
                    elif jogo[0][0] == 'o' and jogo[1][1] == 'o' and jogo[2][2] == 'o':
                        print("\nO jogador 'o' venceu")
                        continua = False
                        break

                    # Caso dê velha na diagonal inversa
                    elif jogo[0][2] == 'o' and jogo[1][1] == 'o' and jogo[2][0] == 'o':
                        print(f"\nO jogador 'o' venceu")
                        continua = False
                        break

    # Indicar se deu empate ou não
    if continua and vezes >= 9:
        print("\nEmpate")
        continua = False

    # Imprimir o jogo da velha após algum jogador vencer
    if not continua:
        print()
        for i in range(3):

            for j in range(3):
                print(jogo[i][j], end='  ')

            print()

    cont += 1
