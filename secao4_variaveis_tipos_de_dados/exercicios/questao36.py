"""
36) Leia a altura e o raio de um cilindro círcular e imprima
o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * raio² * altura, onde r = 3.141592
"""

altura_cilindro = float(input("Digite a altura do cilindro: "))
raio_cilindro = float(input("Digite o raio do cilindro: "))

volume = 3.141592 * (raio_cilindro ** 2) * altura_cilindro

print(f"\nO volume do cilindro:\n3.141592 * {raio_cilindro}² * {altura_cilindro} = {volume}")
