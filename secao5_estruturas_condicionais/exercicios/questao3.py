"""
3) Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print(f'\n{numero ** 0.5}')

else:
    print(f'\n{numero ** 2}')
