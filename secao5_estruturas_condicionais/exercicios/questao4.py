"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada ao número digitado
"""

numero = int(input("Digite um número: "))

if numero > 0:
    print(f'\nO número ao quadrado: {numero ** 2}')
    print(f'Raiz quadrada do número: {numero ** 0.5}')

else:
    print('\nNúmero não é positivo')
