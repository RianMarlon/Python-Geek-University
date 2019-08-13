"""
49) O funcionátios chamado Carlos tem um colega chamado João
que recebe um salário que equivale a um terço do seu salário. Carlos
gosta de fazer aplicações na caderneta de poupança e vai aplicar seu
salário integralmente nela, pois está rendendo 2% ao mês. João aplicará
seu salário integralmente no fundo de renda fixa, que está rendendo 5%
ao mes. Construa um programa que deverá calcular e mostrar a quantidade
de meses necessários para que o valor pertencente a João iguale ou ultrapasse
o valor pertencente a Carlos. Teste com outros valores as taxas.
"""

x = 5000.0
carlos = x
joao = carlos / 3

for i in range(1, 100):
    carlos += carlos * 0.02
    joao += joao * 0.05

    if joao >= carlos:
        print('João: R$%.2f' % joao)
        print('Carlos: R$%.2f' % carlos)
        print(f"Neccesita de {i} meses para que o salário de João iguale ou ultrapasse"
              f" o de Carlos")
        break
