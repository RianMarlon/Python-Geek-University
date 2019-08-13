"""
48) Faça um programa que some os termos de valor par
da sequência de Fibonacci, cujos valores não ultrapassem quatro
milhões.
"""

sequencia1 = 0
sequencia2 = 1

soma = 0

for i in range(1_000_001):
    sequencia1 += sequencia2
    sequencia2 += sequencia1

    if (sequencia1 > 4_000_000) or (sequencia2 > 4_000_000):
        break

    if (sequencia1 % 2 == 0) and (sequencia1 <= 4_000_000):
        soma += sequencia1

    if (sequencia2 % 2 == 0) and (sequencia2 <= 4_000_000):
        soma += sequencia2

print(f"A soma dos valores pares que não ultrapassem quatro milhões: {soma}")
