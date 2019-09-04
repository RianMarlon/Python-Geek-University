"""
20) Faça um programa que leia uma matriz 3 x 6 com valores reais.

(a) Imprima a soma de todos os elementos das colunas ímpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.
"""

matriz = []

for i in range(3):

    elementos = []

    for j in range(6):
        elemento = float(input("Digite um valor: "))
        elementos.append(elemento)

    matriz.append(elementos)

# Variavel para a soma dos elementos das colunas impares
soma_impares = 0
for i in range(3):

    for j in range(6):

        # Assim, a primeira coluna será 1 e não 0
        if (j+1) % 2 == 1:
            soma_impares += matriz[i][j]

print(f"\nSoma dos elementos das colunas ímpares: {soma_impares}")

# Variavel para receber os elementos da segunda e quarta coluna
# e para realizar a média aritmética
media_aritmetica = []
for i in range(3):
    media_aritmetica.append(matriz[i][1])
    media_aritmetica.append(matriz[i][3])

print(f"Média aritmética das colunas 2 e 4: {sum(media_aritmetica) / len(media_aritmetica)}\n")

# Modificando os valores dos elementos da coluna 6
for i in range(3):

    matriz[i][5] = matriz[i][0] + matriz[i][1]

for i in range(3):

    for j in range(6):
        print(matriz[i][j], end='  ')

    print()
