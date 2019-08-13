"""
1) Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0
"""

cont = 0
for i in range(1, 1000):
    if cont >= 5:
        break

    if i % 3 == 0:
        print(i)
        cont += 1
