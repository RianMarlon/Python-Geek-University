"""
40) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados
sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e
escreva o custo ao consumidor

    |      CUSTO DE FÁBRICA          | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | até R$12.000,00                |         5         |    isento      |
    | entre R$12.000,00 e 25.000,00  |        10         |      15        |
    | acima de R$25.000,00           |        15         |      20        |

"""

custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

custo_consumidor = 0.0

print()
if (custo_fabrica > 0) and (custo_fabrica <= 12000):
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.05)
    print("5% da comissão do distribuidor")

elif (custo_fabrica > 12000) and (custo_fabrica <= 25000):
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.1)
    print("10% da comissão do distribuidor")

elif custo_fabrica > 25000:
    custo_consumidor = custo_fabrica + (custo_fabrica * 0.15)
    print("15% da comissão do distribuidor")

else:
    print("Valor inválido")


if (custo_fabrica > 0) and (custo_fabrica <= 12000):
    print("Isento de impostos")

elif (custo_fabrica > 12000) and (custo_fabrica <= 25000):
    custo_consumidor += custo_fabrica * 0.15
    print("15% de impostos sobre o valor de fábrica")

elif custo_fabrica > 25000:
    custo_consumidor += custo_fabrica * 0.2
    print("20% de impostos sobre o valor de fábrica")


print("Valor do carro para o consumidor: %.2f" % custo_consumidor)
