"""
51) Escreva um programa que leia as coordenadas x e y de pontos
no R² e calcule sua distância da origem (0, 0)
"""

import math

x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

resultado = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print("\nSua distância é %.1f" % resultado)
