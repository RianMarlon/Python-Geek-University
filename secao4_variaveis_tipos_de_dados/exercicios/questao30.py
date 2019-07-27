"""
30) Leia um valor em real e a cotação do dólar. Em sequida,
imprima o valor correspondente em dólares
"""

real = float(input("Digite o valor em real: R$"))
cotacao_dolar = float(input("Digite a cotação do dólar: "))

dolar = real * cotacao_dolar

print("\nO valor em dólar(es) é $%.2f" % dolar)
