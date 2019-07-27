"""
9) Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Kelvin. A fórmula de conversão é: K = C + 273.15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

celsius = float(input("Digite a temperatura em graus Celsius °C: "))

kelvin = celsius + 273.15

print("\nA temperatura em graus Kelvin é %.1fK" % kelvin)
