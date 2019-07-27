"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

    A = ((basemaior + basemenor) * altura) / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

base_menor = float(input("Digite o tamanho da base menor do trapézio em cm: "))
base_maior = float(input("Digite o tamanho da base maior do trapézio em cm: "))
altura = float(input("Digite a altura do trapézio em cm: "))

print()
if (base_menor > 0) and (base_maior > 0) and (altura > 0):

    area = ((base_maior + base_menor) * altura) / 2
    print("A área do trapézio é %.1fcm²" % area)

else:
    print("Valor(es) inválido(s)")
