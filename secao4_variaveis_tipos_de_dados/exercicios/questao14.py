"""
14) Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * r / 180, sendo G o ângulo em graus
e R em radianos e r = 3.14.
"""

angulo = float(input("Digite o valor em graus do ângulo: "))

radianos = angulo * 3.14 / 180

print(f"\nO valor do ângulo em radiano é {radianos}")
