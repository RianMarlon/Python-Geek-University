"""
36) Faça um programa que calcule a diferença entre a soma dos quadrados
dos primeiros 100 números naturais e o quadrado da soma. Ex: A soma dos
quadrados dos dez primeiros números naturais é,

    1² + 2² + ... + 10² = 385

O quadrado da soma dos dez primeiros númeors naturais é,

    (1 + 2 + ... + 10)² = 552 = 3025

A diferença entre a soma dos quadrados dos dez primeiros números naturais
e o quadrado da soma é 3025-385 = 2640.
"""

qtd = 100

soma_quadrado = 0
quadrado_soma = 0

for i in range(1, qtd+1):
    soma_quadrado += i ** 2
    quadrado_soma += i

quadrado_soma = quadrado_soma ** 2

print(f'A soma dos quadrados dos {qtd} primeiros números naturais é {soma_quadrado}\n')
print(f'Quadrado da soma dos {qtd} primeiros números naturais é {quadrado_soma}\n')

print(f'A diferença entre a soma dos quadrados dos {qtd} primeiros números naturais'
      f' e o quadrado da soma é {quadrado_soma - soma_quadrado}')
