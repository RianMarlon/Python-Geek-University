"""
31) Faça um programa que calcule o valor de S
    S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""

s = 0.0

termo1 = range(1, 100, 2)
termo2 = range(1, 51)

for i in range(0, 50):
    s += termo1[i]/termo2[i]

print(s)
