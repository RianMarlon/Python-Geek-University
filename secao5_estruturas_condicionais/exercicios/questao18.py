"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básicas, por exemplo). O suário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""

operacao = input("Escolha a operação ['*']['/']['+']['-']: ")

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

print()
if operacao == '*':
    print(f"O resultado do cálculo: {num1 * num2}")

elif operacao == '/':
    print(f"O resultado do cáuclo: {num1 / num2}")

elif operacao == '+':
    print(f"O resultado do cálculo: {num1 + num2}")

elif operacao == '-':
    print(f"O resultado do cáculo: {num1 - num2}")

else:
    print("Operação inválida")