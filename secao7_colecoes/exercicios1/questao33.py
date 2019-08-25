"""
33) Faça um programa que leia um vetor de 15 posições e o compacte, ou
seja, elimine as posições com valor zero. Para isso, todos os elementos
à frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""

vetor = []

for i in range(15):
    vetor.append(int(input("Digite um número: ")))

vetor2 = []

print()
for i in vetor:

    if i != 0:
        vetor2.append(i)

print(vetor2)
