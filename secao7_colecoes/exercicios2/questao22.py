"""
22) Faça um programa que leia duas matrizes A e B
de tamanho 3 x 3 e calcule C = A * B.
"""

matriz_a = []
matriz_b = []

for i in range(3):
    matriz = []

    for j in range(3):
        num = int(input("Digite um número para a primeira matriz: "))

        matriz.append(num)

    matriz_a.append(matriz)

print()
for i in range(3):

    matriz = []

    for j in range(3):
        num = int(input("Digite um número para a segunda matriz: "))

        matriz.append(num)

    matriz_b.append(matriz)

print()

matriz_c = []
for i in range(3):
    matriz = []

    for j in range(3):
        matriz.append(matriz_a[i][j] * matriz_b[i][j])

    matriz_c.append(matriz)

for i in range(3):

    for j in range(3):
        print(matriz_c[i][j], end='  ')

    print()
