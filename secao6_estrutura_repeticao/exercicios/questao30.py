"""
30) Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... + (2n - 1)
"""

termos = 10

calculo1 = 0
calculo2 = 0
calculo3 = 0

for i in range(1, termos + 1):
    calculo1 += i

    if i == termos:
        if i % 2 == 0:
            calculo2 += -i + (2 * termos - 1)

        elif i % 2 == 1:
            calculo2 += i + (2 * termos - 1)
            calculo3 += i

        calculo3 += (2 * termos - 1)

        break

    if i % 2 == 0:
        calculo2 -= i

    elif i % 2 == 1:
        calculo2 += i
        calculo3 += i

print(calculo1)
print(calculo2)
print(calculo3)
