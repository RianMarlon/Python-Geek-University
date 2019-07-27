"""
38) Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""

salario = float(input("Digite o valor do salário do funcionário: "))

novo_salario = salario + (salario*0.25)

print("\nO valor do novo salário:\n%.2f " % novo_salario)
