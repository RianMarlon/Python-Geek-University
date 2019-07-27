"""
40) Uma empresa contrata um encanador a R$30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantida liquida que deverá ser paga. Sabendo-se que são descontandos 8% para imposto de renda.
"""

dias = int(input("Digite o número de dias trabalhados pelo encanador: "))

salario_total = 30.00 * dias
salario_total -= (salario_total * 0.08)

print("\nValor do salário total:\n"
      "R$%.2f" % salario_total)
