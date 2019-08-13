"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""

n = 50
soma_pares = 0
cont = 0

for i in range(1, 1000):
    if i % 2 == 0:
        print(i)
        soma_pares += i
        cont += 1

    if cont >= 50:
        break

print(soma_pares)
