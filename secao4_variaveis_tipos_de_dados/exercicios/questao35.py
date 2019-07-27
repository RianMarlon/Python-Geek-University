"""
35) Sejam a e b os catetos de um triângulo, onde a hipotenusa
é obtida pela equação: hipotenusa = √a² + b². Faça um
programa que receba os valores de a e b e calcule o valor
da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

a = float(input("Digite o valor do cateto a: "))
b = float(input("Digite o valor do cateto b: "))

hipotenusa = (a**2 + b**2) ** 0.5

print(f"\nO valor da hipotenusa:\n √{a}² + {b}² =  {hipotenusa}")
