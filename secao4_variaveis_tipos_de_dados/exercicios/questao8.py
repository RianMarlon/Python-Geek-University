"""
8) Leia uma temperatura em graus Kelvin e apresente-a convertida em
graus Celsius. A fórmula de conversão é: C = K - 273,15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

kelvin = float(input("Digite a temperatura em graus Kelvin K: "))

celsius = kelvin - 273.15

print("\nA temperatura em graus Celsius é %.1f°C" % celsius)
