"""
41) Faça um programa que leia o valor da hora de trabalho (em reais)
e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário.
Adicionando 10% sobre o valor calculado.
"""

valor_hora = float(input("Digite o valor da hora de trabalho (em reais): "))
numero_horas = int(input("Digite o número de horas trabalhadas no mês: "))

valor_pago = valor_hora * numero_horas
valor_pago += valor_pago * 0.10

print("\nO valor a ser pago ao funcionário:\nR$%.2f" % valor_pago)
