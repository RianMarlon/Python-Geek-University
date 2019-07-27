"""
18) Leia um valor de um volume em metros cúbicos m³ e apresente-o
convertido em litros. A fórmula de conversão é: L = 1000 * M,
sendo L o volume em litros e M o volume em metros cúbicos
"""

metros_cubicos = float(input("Digite o valor do volume em metros cúbicos: "))

litros = 1000 * metros_cubicos

print(f"\nO valor do volume em litros é {litros}")
