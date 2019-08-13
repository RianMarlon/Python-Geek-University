"""
61) Faça um programa que calcule o maior número palíndromo feito
a partir do produto de dois números de 3 dígitos. Ex: O maior palíndromo feito
a partir do produto de dois números de dois dígitos é 9009 = 91*99
"""

for i in range(999, 100, -1):

    polindromo = ''

    for j in range(i, 100, -1):
        polindromo = str(i * j)

        if polindromo[::1] == polindromo[::-1]:
            break

    if polindromo[::1] == polindromo[::-1]:
        print(f'{polindromo} = {i} * {j}')
        break
