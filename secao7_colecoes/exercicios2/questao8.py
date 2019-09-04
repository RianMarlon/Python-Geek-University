"""
8) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que
estão acima da diagonal principal.
"""

lista1 = []
for i in range(3):

    lista2 = []
    for j in range(3):
        num = int(input("Digite um valor: "))

        lista2.append(num)

    lista1.append(lista2)

print()

soma = 0
for i in range(3):

    for j in range(3):

        # Imprimindo a matriz escrita feita pelo usuário
        print(f"{lista1[i][j]}", end='  ')

        if i != 0 and i == j:

            # Pegando os valores que estão acima da linha onde se encontra a coluna da diagonal
            for k in range(1, i + 1):
                soma += lista1[i - k][j]

    print()

print(f"\nA soma dos elementos que estão acima da diagonal principal: {soma}")
