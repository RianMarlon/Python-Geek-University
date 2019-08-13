"""
21) Faça um programa que receba dois números. Calcule e mostre:
    - A soma dos números pares desse intervalo de números, incluindo
os números digitados;
    - A multiuplicação dos números ímpares desse intervalo, incluindo
os digitados;
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma_pares = 0
multi_impares = 1

if num1 >= num2:

    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            soma_pares += i

        elif i % 2 == 1:
            multi_impares *= i

        elif (i % 2 == -1) and (i < 0):
            multi_impares *= i

        else:
            print("Erro!")

elif num2 > num1:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            soma_pares += i

        elif i % 2 == 1:
            multi_impares *= i

        elif (i % 2 == -1) and (i < 0):
            multi_impares *= i

        else:
            print("Erro!")

print()
print(f"A soma dos números pares no intervalo dos números: {soma_pares}")
print(f"A multiplicação dos números ímpares no intervalo\ndos números digitados:{multi_impares}")
