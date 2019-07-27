"""
15) Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/r, sendo G o ângulo
em graus e R em radianos e r = 3.14.
"""

radianos = float(input("Digite o valor do ângulo em radianos: "))

graus = radianos * 180 / 3.14

print(f"\nO valor do ângulo em graus é {graus}")
