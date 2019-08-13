"""
18) Escreva um algoritmo que leia certa quantidade de números
e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

n = int(input("Digite a quantidade de números a serem lidos: "))

maior = 0

print()
for i in range(1, n+1):
    num = int(input(f"Digite o {i}° número: "))

    if i == 1:
        maior = num

    elif num > maior:
        maior = num

print()
print(f"O maior número: {maior}")