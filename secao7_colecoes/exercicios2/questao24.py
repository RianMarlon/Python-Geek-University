"""
24) Na matriz de 20 x 20 abaixo, quatro números ao longo de uma linha diagonal foram
marcadas em negrito. O produto deses números é 26 * 63 * 78 * 14 = 1788696.

Qual é o maior produto de quatro números adjacentes em qualquer direção
(cima, baixo, equerda, direita, ou na diagonal) na matriz de 20 x 20?
"""

from random import randint

matriz_grande = []

for i in range(20):

    matriz = []

    for j in range(20):
        matriz.append(randint(0, 99))

    matriz_grande.append(matriz)

for i in range(20):

    for j in range(20):
        print(matriz_grande[i][j], end='  ')

    print()

matriz_cima = []
matriz_baixo = []
matriz_esquerda = []
matriz_direita = []
matriz_diagonal = []

# Será 17 linhas com 20 colunas cada (de 4 em 4)
for i in range(19, -1, -1):

    if i >= 2:
        num = 1

        # Pulando de 4 em 4 (de baixo para cima) as linhas de cada coluna e realizando o calculo
        for j in range(20):
            num = matriz_grande[i][j] * matriz_grande[i-1][j] * matriz_grande[i-2][j] * matriz_grande[i-3][j]

            matriz_cima.append(num)

print()
print(len(matriz_cima))

# Será 17 linhas com 20 colunas cada (de 4 em 4)
for i in range(20):

    if i <= 16:
        num = 1

        # Pulando de 4 em 4 (de cima para baixo) as linhas de cada coluna e realizando o calculo
        for j in range(20):
            num = matriz_grande[i][j] * matriz_grande[i+1][j] * matriz_grande[i+2][j] * matriz_grande[i+3][j]

            matriz_baixo.append(num)

print()
print(len(matriz_baixo))

# Será 20 linhas com 17 colunas cada (de 4 em 4)
for i in range(20):
    num = 1

    # Pulando de 4 em 4 (da esquerda para direita) as colunas de cada linha e realizando o calculo
    for j in range(20):

        if j <= 16:
            num = matriz_grande[i][j] * matriz_grande[i][j+1] * matriz_grande[i][j+2] * matriz_grande[i][j+3]

            matriz_direita.append(num)

print()
print(len(matriz_direita))

# Será 20 linhas com 17 colunas cada (de 4 em 4)
for i in range(20):
    num = 1

    # Pulando de 4 em 4 (da direita para a esquerda) as colunas de cada linha e realizando o calculo
    for j in range(19, -1, -1):

        if j >= 2:
            num = matriz_grande[i][j] * matriz_grande[i][j-1] * matriz_grande[i][j-2] * matriz_grande[i][j-3]

            matriz_esquerda.append(num)

print()
print(len(matriz_esquerda))

for i in range(20):
    num = 1

    # Percorrendo a diagonal principal
    for j in range(20):

        # A partir da linha 17 não se faz mais um conjunto de 4 elementos na diagonal
        # A partir da coluna 17 não se faz mais um conjunto de 4 elementos na diagonal
        if (i <= 16) and (j <= 16):
            num = matriz_grande[i][j] * matriz_grande[i+1][j+1] * matriz_grande[i+2][j+2] * matriz_grande[i+3][j+3]

        matriz_diagonal.append(num)

    # Percorrendo a diagonal secundaria
    for j in range(19, -1, -1):

        # A partir da linha 17 não se faz mais um conjunto de 4 elementos na diagonal
        # A partir da coluna 4 não se faz mais um conjunto de 4 elementos na diagonal
        if (i <= 16) and (j >= 3):
            num = matriz_grande[i][j] * matriz_grande[i+1][j-1] * matriz_grande[i+2][j-2] * matriz_grande[i+3][j-3]

        matriz_diagonal.append(num)

print()
print(len(matriz_diagonal))

produtos = [max(matriz_cima), max(matriz_baixo), max(matriz_esquerda), max(matriz_direita), max(matriz_diagonal)]

maior_produto = max(produtos)

print(f'\nO maior produto é {maior_produto}')
