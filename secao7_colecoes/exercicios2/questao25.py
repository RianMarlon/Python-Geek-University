"""
25) Faça um programa  para determnar a próxima jogada em um Jogo da Velha.
Assumir que o tabuleiro é representado por uma matriz de 3 x 3, onde cada
posição representa uma das casas do tabuleiro. A matriz pode conter os
seguintes valores -1, 0, 1 representando respectivamente uma casa contendo uma
peça minha (-1), uma casa vazia do tabuleiro (0), e uma casa contendo uma peça
do seu oponente (1)

Exemplo:

    -1  |  1  |  1
    -1  | -1  |  0
     0  |  1  |  0
"""

jogo = []

for i in range(3):

    velha = []
    for j in range(3):
        velha.append(0)

    jogo.append(velha)

cont = 1

# Indicador se o jogo continua ou não
continua = True
vezes = 0

while continua:

    # Imprimir como o jogo está antes de cada jogada
    for i in range(3):

        for j in range(3):
            print(jogo[i][j], end='  ')

        print()

    if cont % 2 == 0:
        print("\nVez do jogador '-1'")

    elif cont % 2 == 1:
        print("\nVez do jogador '1'")

    linha = int(input("Digite a linha que você deseja colocar a peça (1 à 3): "))
    if (linha >= 1) and (linha <= 3):
        coluna = int(input("Digite a coluna que você deseja colocar a peça (1 à 3): "))

        if (coluna >= 1) and (coluna <= 3):

            if cont % 2 == 0:

                if jogo[linha-1][coluna-1] == 0:
                    jogo[linha-1][coluna-1] = -1

                    vezes += 1

                else:
                    print("Perdeu a vez: existe uma peça nesse local\n")

            elif cont % 2 == 1:
                if jogo[linha-1][coluna-1] == 0:
                    jogo[linha-1][coluna-1] = 1

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

                # Caso dê velha na horizontal
                if jogo[j][0] == i and jogo[j][1] == i and jogo[j][2] == i:
                    print(f"\nO jogador '{i}' venceu")
                    continua = False
                    break

                # Caso dê velha na vertical
                elif jogo[0][j] == i and jogo[1][j] == i and jogo[2][j] == i:
                    print(f"\nO jogador '{i}' venceu")
                    continua = False
                    break

                # Caso dê velha na diagonal principal
                elif jogo[0][0] == i and jogo[1][1] == i and jogo[2][2] == i:
                    print(f"\nO jogador '{i}' venceu")
                    continua = False
                    break

                # Caso dê velha na diagonal inversa
                elif jogo[0][2] == i and jogo[1][1] == i and jogo[2][0] == i:
                    print(f"\nO jogador '{i}' venceu")
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
