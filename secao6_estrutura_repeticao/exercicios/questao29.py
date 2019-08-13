"""
29) Escreva um programa para calcular o valor da série,
para 5 termos.

    S = 0 + 1/2! + 2/4! + 3/6! + ...
"""

termos = 5

s = 0
fatores = 1

for i in range(1, termos + 1):
    fatores = 2 * i

    for j in range(1, fatores):
        fatores *= j

    s += i / fatores

print(f"Valor da série: {s}")
