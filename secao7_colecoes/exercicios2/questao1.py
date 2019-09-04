"""
1) Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""

lista1 = []

cont = 0
for i in range(4):
    lista2 = []

    for j in range(4):
        num = int(input("Digite um número: "))
        lista2.append(num)

        if num > 10:
            cont += 1

    lista1.append(lista2)

print(f"\nA matriz 4 x 4 possui {cont} valores maiores que 10")
print(lista1)
