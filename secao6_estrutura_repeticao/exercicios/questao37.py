"""
37) Escreve um programa que verifique quais os números entre 1000 e 9999
(inclusive) possuem a propriedade seguinte: a soma dos dois dígitos de
mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado
é igual ao próprio número. Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""

soma = 0
for i in range(1000, 10000):
    numero = str(i)
    soma = int(numero[0] + numero[1]) + int(numero[2] + numero[3])

    if soma ** 2 == i:
        print(i)
