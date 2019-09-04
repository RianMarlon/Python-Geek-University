"""
13) Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os
elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada.
"""

from random import randint

lista1 = []

for i in range(4):

    lista2 = []
    for j in range(4):
        lista2.append(randint(1, 20))

    lista1.append(lista2)

# Imprimindo a matriz gerada
for i in range(4):

    for j in range(4):
        print(lista1[i][j], end='  ')

    print()

print()
cont = 0
for i in range(4):

    for j in range(4):
        if i != 0 and i == j:

            # Pegando os valores que estão acima da linha onde se encontra a coluna da diagonal e adicionando 0
            for k in range(1, i+1):
                lista1[i-k][j] = 0

# Imprimindo a matriz tranformada
for i in range(4):

    for j in range(4):
        print(lista1[i][j], end='  ')

    print()
