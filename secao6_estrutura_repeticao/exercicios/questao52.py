"""
52) Escreva um programa que receba como entrada o valor do saque
realizado pelo cliente de um banco e retorne quantas notas de cada valor
serão necessárias para atender ao saque com a menor quantidade de notas possível.
Serão utilizadas notas de 100, 50, 20, 10, 5, 2, 1 real.
"""

valor_saque = int(input("Digite o valor do saque: "))

print()
if valor_saque > 0:

    cont100 = 0
    cont50 = 0
    cont20 = 0
    cont10 = 0
    cont5 = 0
    cont2 = 0
    cont1 = 0

    while True:

        if (valor_saque - 100) >= 0:
            valor_saque -= 100
            cont100 += 1

        elif (valor_saque - 50) >= 0:
            valor_saque -= 50
            cont50 += 1

        elif (valor_saque - 20) >= 0:
            valor_saque -= 20
            cont20 += 1

        elif (valor_saque - 10) >= 0:
            valor_saque -= 10
            cont10 += 1

        elif (valor_saque - 5) >= 0:
            valor_saque -= 5
            cont5 += 1

        elif (valor_saque - 2) >= 0:
            valor_saque -= 2
            cont2 += 1

        elif (valor_saque - 1) >= 0:
            valor_saque -= 1
            cont1 += 1

        else:
            print(f"Quantidade de notas de 100: {cont100}\n"
                  f"Quantidade de notas de 50: {cont50}\n"
                  f"Quantidade de notas de 20: {cont20}\n"
                  f"Quantidade de notas de 10: {cont10}\n"
                  f"Quantidade de notas de 5: {cont5}\n"
                  f"Quantidade de notas de 2: {cont2}\n"
                  f"Quantidade de notas de 1: {cont1}")
            break

else:
    print("Valor de saque inválido")
