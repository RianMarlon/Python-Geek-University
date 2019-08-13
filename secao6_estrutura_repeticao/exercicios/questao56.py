"""
56) Faça um programa que calcule a soma de todos os números primos
abaixo de dois milhões.
"""

qtd = 2000000

soma = 0

for i in range(1, qtd):
    cont = 0

    for j in range(1, i+1):
        if (i % 1 == 0) and (i % j == 0):
            cont += 1

    if cont <= 2:
        soma += i

print(f"A soma de todos os números primos abaixo de dois milhões: {soma}")
