"""
42) Faça um programa que leia um conjunto não determinado de valores,
um de cada vez, e escreva para cada um dos valores lidos, o quadrado
o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""

while True:
    numero = int(input("Digite um valor: "))

    print()
    if numero > 0:
        print(f"O quadrado de {numero}: {numero ** 2}")
        print(f"O cubo de {numero}: {numero ** 3}")
        print(f"A raiz quadrada de {numero}: {numero ** (1/2)}")

        print()

    else:
        print("O valor não pode ser negativo ou zero!")
        break
