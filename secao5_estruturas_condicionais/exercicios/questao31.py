"""
31) Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostre qual a classificação
dessa pessoa.

    |    Altura    |                       Peso                       |
    |              |Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90  |
    |Menor que 1,20|   A   |             D             |      G       |
    |De 1,20 a 1,70|   B   |             E             |      H       |
    |Maior que 1,70|   C   |             F             |      I       |
"""

altura = float(input("Digite a altura(em metros): "))
peso = float(input("Digite o peso(kg): "))

if (altura <= 1.20) and (peso <= 60):
    print("Classificação: A")

elif (altura > 1.20) and (altura <= 1.70) and (peso <= 60):
    print("Classificação: B")

elif (altura > 1.70) and (peso <= 60):
    print("Classificação: C")

elif (altura <= 1.20) and (peso > 60) and (peso <= 90):
    print("Classificação: D")

elif (altura > 1.20) and (altura <= 1.70) and (peso > 60) and (peso <= 90):
    print("Classificação: E")

elif (altura > 1.70) and (peso > 60) and (peso <= 90):
    print("Classificação: F")

elif (altura <= 1.20) and (peso > 90):
    print("Classificação: G")

elif (altura > 1.20) and (altura <= 1.70) and (peso > 90):
    print("Classificação: H")

elif (altura > 1.70) and (peso > 90):
    print("Classificação: I")

else:
    print("Erro inesperado!")