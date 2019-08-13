"""
20) Ler uma sequência de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de valores
pares. O processo termina quando for digitado o número 1000.
"""

num = 0
cont_numeros = 0
cont_pares = 0

while num != 1000:
    num = int(input("Digite um número: "))

    if (num > 0) and (num % 2 == 0) or (num < 0) and (num % 2 == -1):
        cont_pares += 1

    cont_numeros += 1

print()
print(f"Número de dados lidos: {cont_numeros}")
print(f"Número de valores pares: {cont_pares}")
