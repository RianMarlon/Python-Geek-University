"""
46) Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o
chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta
o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
from random import randint

numero = randint(1, 1000)

while True:
    tentativa = int(input("Tente acertar o número aleatório: "))

    print()
    if tentativa > numero:
        print("O número é menor. Tente novamente!\n")

    elif tentativa < numero:
        print("O número é maior. Tente novamente!\n")

    elif tentativa == numero:
        print("Parabéns, você acertou!")
        break
