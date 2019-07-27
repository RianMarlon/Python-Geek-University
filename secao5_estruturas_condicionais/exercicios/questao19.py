"""
19) Faça um programa para verificar se um determinado número
inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""

numero = int(input("Digite um número: "))

if numero % 3 == 0 and not (numero % 5 == 0):
    print("Divisível por 3.")

elif numero % 5 == 0 and not(numero % 3 == 0):
    print("Divisível por 5.")

else:
    print("Não divisível por 3 ou 5 / Não pode ser divisível pelos dois ")