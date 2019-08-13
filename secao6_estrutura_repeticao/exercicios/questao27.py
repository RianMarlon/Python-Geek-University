"""
27) Em Matemática, o número harmônico designado por H(n) define-se
como sendo a soma da série harmônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""

n = int(input("Digite um valor inteiro e positivo: "))

h = 1

if n > 0:
    for i in range(1, n+1):
        h += 1/i

    print(f"O valor de H(n): {h}")

else:
    print("O valor deve ser positivo!")
