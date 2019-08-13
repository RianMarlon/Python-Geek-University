"""
43) Faça um programa que leia um número inderterminado de idades de
indivíduos (pare quando for informada a idade 0), e calcule a idade
média desse grupo.
"""

idade = int(input("Digite uma idade: "))

if idade != 0:
    media = idade
    cont = 1

    while True:
        idade = int(input("Digite uma idade: "))

        if idade != 0:
            media += idade
            cont += 1

        else:
            break

    print()
    print("Idade média do grupo: %.0f " % (media / cont))

else:
    print()
    print("A idade não pode ser zero!")
