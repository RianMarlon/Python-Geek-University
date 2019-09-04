"""
21) Faça um programa que leia duas matrizes 2 x 2 com valores reais.
Ofereça ao usuário um menu de opções:

(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes

"""

matriz1 = []

# A primeira matriz 2 x 2
for i in range(2):
    matriz2 = []

    for j in range(2):
        num = int(input("Digite um número para a primeira matriz: "))
        matriz2.append(num)

    matriz1.append(matriz2)

print()

matriz2 = []

# A segunda matriz 2 x 2
for i in range(2):
    matriz3 = []

    for j in range(2):
        num = int(input("Digite um número para a segunda matriz: "))
        matriz3.append(num)

    matriz2.append(matriz3)

while True:
    opcao = str(input("\nMenu de opções:\n\n"
                      "(a) somar as duas matrizes\n"
                      "(b) subtrair a primeira matriz da segunda\n"
                      "(c) adicionar uma constante às duas matrizes\n"
                      "(d) imprimir as matrizes\n\n"
                      "Digite apenas a letra referente a opção que você deseja: "))

    print()

    if opcao.lower() == 'a':
        soma_matrizes = []

        print("A soma dos elementos de mesma posição da matriz:")

        for i in range(2):

            soma = []

            for j in range(2):
                soma.append(matriz1[i][j] + matriz2[i][j])

            soma_matrizes.append(soma)

        for i in range(2):

            for j in range(2):
                print(soma_matrizes[i][j], end='  ')

            print()

    elif opcao.lower() == 'b':
        subtrair_matrizes = []

        print("A subtração dos elementos de mesma posição da matriz:")

        for i in range(2):

            subtrair = []

            for j in range(2):
                subtrair.append(matriz1[i][j] - matriz2[i][j])

            subtrair_matrizes.append(subtrair)

        for i in range(2):

            for j in range(2):
                print(subtrair_matrizes[i][j], end='  ')

            print()

    elif opcao.lower() == 'c':
        constante = int(input("Digite uma constante inteira: "))

        for i in range(2):

            for j in range(2):
                matriz1[i][j] += constante
                matriz2[i][j] += constante

    elif opcao.lower() == 'd':

        print("Matriz 1:")
        for i in range(2):

            for j in range(2):
                print(matriz1[i][j], end='  ')

            print()

        print("\nMatriz 2:")
        for i in range(2):

            for j in range(2):
                print(matriz2[i][j], end='  ')

            print()

    else:
        print("ENCERRADO!")
        break
