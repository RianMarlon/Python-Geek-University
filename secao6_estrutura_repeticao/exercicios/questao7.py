"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""

media = 0
soma = 0
cont = 10
for i in range(1, 11):
    num = int(input(f"Digite o {i}° valor: "))
    if num < 0:
        cont -= 1

    else:
        soma += num

    if i >= 10:
        media = soma / cont

print()
print(f"Média: {media}")
