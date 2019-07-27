"""
19) Leia um valor de um volume em litros e apresente-o
convertido em metros cúbicos m³. A fórmula de conversão é: M = L/1000,
sendo o L o volume em litros e M o volume em metros cúbicos.
"""

litros = float(input("Digite o valor do volume em litros: "))

metros_cubicos = litros / 1000

print(f"\nO valor do volume em metros cúbicos é {metros_cubicos}")