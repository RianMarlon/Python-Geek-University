"""
5) Faça um programa que receba um número inteiro e verifique se este número é
par ou ímpar.
"""

numero = int(input("Digite um número: "))

print()
if numero % 2 == 0:
    print("Par")

elif numero % 2 == 1:
    print("Ímpar")

else:
    print("Erro inesperado")
