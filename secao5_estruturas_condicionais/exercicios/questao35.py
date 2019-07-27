"""
35) Leia uma data e determine se ela é válida. Ou seja, verifique se o
mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem
29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""

dia = int(input("Digite o dia do mês: "))
mes = int(input("Digite o mês do ano: "))
ano = int(input("Digite o ano: "))

print()
if ano != 0:
    if mes == 1:

        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 2:

        if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
            if (dia >= 1) and (dia <= 29):
                print("Data válida")
            else:
                print("Dia inválido")

        else:
            if (dia >= 1) and (dia <= 28):
                print("Data válida")
            else:
                print("Dia inválido")

    elif mes == 3:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 4:
        if (dia >= 1) and (dia <= 30):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 5:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 6:
        if (dia >= 1) and (dia <= 30):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 7:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 8:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 9:
        if (dia >= 1) and (dia <= 30):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 10:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 11:
        if (dia >= 1) and (dia <= 30):
            print("Data válida")

        else:
            print("Dia inválido")

    elif mes == 12:
        if (dia >= 1) and (dia <= 31):
            print("Data válida")

        else:
            print("Dia inválido")

    else:
        print("Número do mês inválido")

else:
    print("O ano não pode ser 0")