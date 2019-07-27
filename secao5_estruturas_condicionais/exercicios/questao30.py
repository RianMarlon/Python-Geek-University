"""
30) Faça um programa que receba três números e mostre-o em ordem crescente.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print()
if (num1 >= num2) and (num2 >= num3):
    print(f"Ordem crescente: {num3}-{num2}-{num1}")

elif (num1 >= num3) and (num3 >= num2):
    print(f"Ordem crescente: {num2}-{num3}-{num1}")

elif (num2 >= num1) and (num1 >= num3):
    print(f"Ordem crescente: {num3}-{num1}-{num2}")

elif (num2 >= num3) and (num3 >= num1):
    print(f"Ordem crescente: {num1}-{num3}-{num2}")

elif (num3 >= num1) and (num1 >= num2):
    print(f"Ordem crescente: {num2}-{num1}-{num3}")

elif (num3 >= num2) and (num2 >= num1):
    print(f"Ordem crescente: {num1}-{num2}-{num3}")

else:
    print("Erro inesperado!")
