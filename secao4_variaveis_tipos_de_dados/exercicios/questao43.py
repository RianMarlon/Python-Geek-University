"""
43) Escreva um programa de ajuda para vendedores. A partir de um valor
total lido, mostre:
 - O total a pagar com desconto de 10%
 - O valor de cada parcela, no parcelamento de 3x sem juros;
 - A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
 - A comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total)
"""

valor = float(input("Digite o valor: "))

valor_desconto = valor - (valor * 0.10)

valor_parcela = valor / 3
valor_a_vista = valor_desconto - (valor_desconto * 0.05)
valor_parcelado = valor - (valor * 0.05)

print(f"\nO total a pagar com 10% de desconto : {valor_desconto}")
print("O valor de cada parcela, no parcelamento de 3x sem juros: %.1f" % valor_parcela)
print(f"O comissão do vendedor, no caso da venda ser a vista\n"
      f"(5% sobre o valor com desconto): {valor_a_vista}")
print(f"A comissão do vendedor, no caso da venda ser parcelada\n"
      f"(5% sobre o valor total): {valor_parcelado}")
