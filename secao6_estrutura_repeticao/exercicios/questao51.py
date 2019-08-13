"""
51) Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais.
Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem
ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
"""

ano_atual = 2019
ano_inicial = 1995

aumento = 1.5

for i in range(ano_inicial, ano_atual+1):

    salario = 2000

    if i == ano_inicial:
        pass

    elif (i > ano_inicial) and (i < ano_atual):
        salario += salario * (aumento / 100)
        aumento *= 2

    elif i == ano_atual:
        salario += salario * (aumento / 100)
        print("Ano: %d -> Salário: %.2f" % (i, salario))
