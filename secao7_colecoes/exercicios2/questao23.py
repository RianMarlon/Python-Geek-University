"""
23) Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
"""

matriz_a = []

for i in range(3):
    matriz = []

    for j in range(3):
        num = int(input("Digite um número para a matriz: "))

        matriz.append(num)

    matriz_a.append(matriz)

print()

matriz_b = []
for i in range(3):
    matriz = []

    for j in range(3):
        matriz.append(matriz_a[i][j] ** 2)

    matriz_b.append(matriz)

for i in range(3):

    for j in range(3):
        print(matriz_b[i][j], end='  ')

    print()
