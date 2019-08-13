"""
34) Faça um programa que calcule o menor número divisível por cada
um dos números de 1 a 15? Ex: 2520 é o menor número que pode ser
dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

menor = 0
cont = 0

for i in range(1, 999999):

    for j in range(1, 16):
        if i % j == 0:
            cont += 1

        if cont >= 15:
            menor = i

    if menor > 0:
        print(menor)
        break

    cont = 0
