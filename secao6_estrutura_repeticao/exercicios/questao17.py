"""
17) Faça um programa que leia um número inteiro positivo
n e calcule a soma dos n primeiros números naturais.
"""

num = int(input("Digite um número inteiro e positivo: "))

soma = 00

print()
if num > 0:
    print(f"A soma dos {num} primeiros números naturais:")
    for i in range(1, num*num):
        if i <= num:
            soma += i

        else:
            break

    print(soma)

else:
    print("O número não pode ser zero ou negativo!")
