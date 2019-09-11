"""
16) Leia um valor de comprimento em polegadas e apresente-o convertido
em centímetros. A fórmula de conversão é: P = C / 2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""

polegadas = float(input("Digite o comprimeto em polegadas: "))

centimetros = polegadas * 2.54

print("\nO comprimento em centímetros é %.1f" % centimetros)
