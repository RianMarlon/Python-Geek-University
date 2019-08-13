"""
57) Faça um programa que some os números primos existem entre a
e b, onde a e b são números informados pelo usuário.
"""

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))

print()
if a > b:
    soma = 0

    for i in range(b, a+1):
        cont = 0

        for j in range(1, i+1):
            if (i % 1 == 0) and (i % j == 0):
                cont += 1

        if cont <= 2:
            soma += i

    print(f"A soma dos números primos no intervalo de {b} à {a} é {soma}")

elif b > a:
    soma = 0

    for i in range(a, b+1):
        cont = 0

        for j in range(1, i + 1):
            if (i % 1 == 0) and (i % j == 0):
                cont += 1

        if cont <= 2:
            soma += i

    print(f"A soma dos números primos no intervalo de {a} à {b} é {soma}")

else:
    print("Valores inválidos")
