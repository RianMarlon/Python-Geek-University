"""
7) Gerar e imprimir uma matriz de tamanho de 10 x 10, onde
seus elementos são da forma:

A[i][j] = 2i + 7j - 2 se i < j:
A[i][j] = 3i² - 1 se i = j:
A[i][j] = 1i³ - 5j² + 1 se i > j:
"""

lista1 = []
for i in range(10):
    lista2 = []

    for j in range(10):
        calculo = 0
        if i < j:
            calculo = (2 * i) + (7 * j) - 2
            lista2.append(calculo)

        elif i == j:
            calculo = (3 * i) ** 2 - 1
            lista2.append(calculo)

        elif i > j:
            calculo = (4 * i) ** 3 - (5 * j) ** 2 + 1
            lista2.append(calculo)

    lista1.append(lista2)

print(lista1)

for i in range(10):
    for j in range(10):
        print(lista1[i][j], end='  ')

    print()
