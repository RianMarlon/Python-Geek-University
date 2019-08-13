"""
53) Escreva um programa que leia um número inteiro positivo n e em
seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 10 21

"""

n = int(input("Digite uma quantidade: "))

if n > 0:
    cont = 0

    for i in range(1, n+1):
        cont += 1
        for j in range(1, i+1):
            if j == 1:
                print(f"{cont} ", end="")
            else:
                cont += 1
                print(f"{cont} ", end="")
        print()

else:
    print("Quantidade inválida")
