"""
6) Escreva um programa que, dados dois números inteiro, mostre na tela
o maior deles, assim como a diferença existentes entre ambos.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print()
if num1 > num2:
    print(f'O maior número é {num1} e a diferença entre os dois números é {num1 - num2}')

elif num2 > num1:
    print(f'O maior número é o {num2} e a diferença entre os dois números é {num2 - num1}')

else:
    print('Erro inesperado')
