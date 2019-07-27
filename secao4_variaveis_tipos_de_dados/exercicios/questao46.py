"""
46) Faça um programa que leia um número inteiro positivo de
três digitos (de 100 a 999). Gere outro número formado pelos
dígitos invertidos do número lido. Exemplo:

    NúmeroLido = 123
    NúmeroGerado = 321
"""

numero = int(input("Digite um número: "))

numero_gerado = str(numero)[::-1]

print(f"\nO número gerado: {numero_gerado}")
