"""
15) Usando swith, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2,
e assim por diante.
"""

numero = int(input("Digite um número referente ao dia da semana: "))

print()
if (numero >= 1) and (numero <= 7):
    if numero == 1:
        print("Domingo")

    elif numero == 2:
        print("Segunda-feira")

    elif numero == 3:
        print("Terça-feira")

    elif numero == 4:
        print("Quarta-feira")

    elif numero == 5:
        print("Quinta-feira")

    elif numero == 6:
        print("Sexta-feita")

    else:
        print("Sabádo")

else:
    print("Dia inválido")
