"""
2) Leia um número fornecido pelo usuário. Se esse númerro for positivo,
calcule a raiz quadrada do número. Se o número for negativo, mostre
uma mensagem dizendo que o número é inválido.
"""

numero = int(input("Digite um número: "))

if numero > 0:
    print(f"\n{numero ** 2}")

elif numero < 0:
    print("\nNúmero inválido")

else:
    print("\nNúmero igual a zero")
