"""
6) Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores
valores de cada posição das matrizes lidas.
"""

lista1 = []
for i in range(4):
    lista2 = []

    for j in range(4):
        num = int(input("Digite um valor para a primeira matriz: "))
        lista2.append(num)

    lista1.append(lista2)

print()

lista2 = []
for i in range(4):
    lista3 = []

    for j in range(4):
        num = int(input("Digite um valor para a segunda matriz: "))
        lista3.append(num)

    lista2.append(lista3)

print()

lista3 = []
# Pega os maiores valores de cada matriz que está dentro da matriz
for i in range(4):

    lista3.append(max(lista1[i]))

for i in range(4):

    lista3.append(max(lista2[i]))

print(lista3)
