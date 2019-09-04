"""
2) Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0
os demais elementos. Escreva ao final matriz obtida
"""

lista1 = []

for i in range(5):
    lista2 = []

    for j in range(5):
        if j == i:
            lista2.append(1)

        else:
            lista2.append(0)
    lista1.append(lista2)

for i in range(5):

    for j in range(5):
        print(lista1[i][j], end='  ')

    print()

print()
print(lista1)
