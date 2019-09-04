"""
4) Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e coluna)
do maior valor.
"""

lista1 = []

maior = -9999999999
linha = 0
coluna = 0

for i in range(4):
    lista2 = []

    for j in range(4):
        num = int(input("Digite um número: "))

        if num > maior:
            maior = num
            linha = i
            coluna = j

        lista2.append(num)

    lista1.append(lista2)

print(f"\n{lista1}")

for i in range(4):

    for j in range(4):
        print(f"{lista1[i][j]}", end='  ')

    print()

print(f"\nA localização do maior valor -> linha = {linha}; coluna = {coluna} ")
