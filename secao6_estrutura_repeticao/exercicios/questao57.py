"""
57) Faça um programa que conte quantos números primos existem entre a
e b, onde a e b são números informados pelo usuário.
"""

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))

print()
if a > b:
    qtd = 0

    for i in range(b, a+1):
        cont = 0

        for j in range(1, i+1):
            if (i % 1 == 0) and (i % j == 0):
                cont += 1

        if cont <= 2:
            qtd += 1

    print(f"A quantidade de números primos no intervalo de {b} à {a} é {qtd}")

elif b > a:
    qtd = 0

    for i in range(a, b+1):
        cont = 0

        for j in range(1, i + 1):
            if (i % 1 == 0) and (i % j == 0):
                cont += 1

        if cont <= 2:
            qtd += 1

    print(f"A quantidade de números primos no intervalo de {a} à {b} é {qtd}")

else:
    print("Valores inválidos")
