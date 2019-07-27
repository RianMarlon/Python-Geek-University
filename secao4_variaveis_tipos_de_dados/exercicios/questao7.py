"""
7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é: C = (F-32.0)*5.0/9.0,
sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit °F: "))

celsius = (fahrenheit-32.0)*5.0/9.0

print("A temperatura em graus Celsius é %.1f°C" % celsius)
