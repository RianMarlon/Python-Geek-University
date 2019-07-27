"""
1) Faça um programa que receba dois números e mostre qual deles é o maior.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"\nO número {num1} é maior que o número {num2}.")

elif num2 > num1:
    print(f"\nO número {num2} é maior que o número {num1}.")

else:
    print("\nOs dois números possuem o mesmo valor.")
