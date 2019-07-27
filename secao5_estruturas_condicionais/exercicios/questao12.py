"""
12) Leu um número inteiro. Se o número lido for negativo, escreva a mensagem
'Número inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
from math import log10

numero = int(input("Digite um número: "))

print()
if numero > 0:
    print(f'O logaritmo desse número é {log10(numero)}')

else:
    print("Número inválido")