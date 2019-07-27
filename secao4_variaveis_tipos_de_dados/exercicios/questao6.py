"""
6) Leia uma temperatura em gruas Celsius e apresente-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

celsius = float(input("Digite a temperatura em graus Celsius °C: "))

fahrenheit = celsius*(9.0/5.0)+32


print("A temperatura em graus Fahrenheit é %.2f°F" % fahrenheit)
