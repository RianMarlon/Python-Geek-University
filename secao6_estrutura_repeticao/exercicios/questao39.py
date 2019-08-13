"""
39) Faça um programa que calcule a área de um triângulo, cuja base e altura
são fornecida pelo usuário. Esse programa não pode permitir a entrada de dados inválidos,
ou seja, medidas menores ou iguais a 0.
"""

base = int(input("Digite o tamanho da base do triângulo: "))

if base > 0:
    altura = int(input("Digite o tamanho da altura do triângulo: "))
    print()

    if altura > 0:
        area_triangulo = (base * altura) / 2
        print(f"A aréa do triângulo é {area_triangulo}")

    else:
        print("Altura inválida!")

else:
    print()
    print("Base inválida!")
