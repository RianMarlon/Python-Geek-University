"""
3) Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha
e da coluna de cada elemento. Em seguida, imprima na tela a matriz.
"""

lista1 = []

for i in range(4):
    lista2 = []

    for j in range(4):
        lista2.append(i * j)

    lista1.append(lista2)

for i in range(4):

    for j in range(4):
        print(lista1[i][j], end='  ')

    print()

print()
print(lista1)
