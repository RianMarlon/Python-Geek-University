"""
54) Faça um programa que receba um número inteiro maior do que 1,
e verifique se o número fornecido é primo ou não.
"""

numero = int(input("Digite um número: "))

cont = 0

if numero > 1:
    for i in range(1, numero+1):
        if (numero % 1 == 0) and (numero % i == 0):
            cont += 1

    if cont <= 2:
        print("Número primo")

    else:
        print("Não é número primo")
