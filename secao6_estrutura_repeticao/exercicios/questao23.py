"""
23) Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

num = int(input("Digite um número: "))

print()
if num > 0:
    print("Os divisores desse número são: ")
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

else:
    print("O número deve ser positivo!")
