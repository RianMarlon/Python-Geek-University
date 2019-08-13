"""
26) Faça um algoritmo que encontre o primeiro múltiplo de 11, 13
ou 17 após um número dado.
"""

num = int(input("Digite um número: "))

lista = [11, 13, 17]

print()
print(f"Primeiro múltiplo de 11, 13 ou 17 de {num}:")
for x, y in enumerate(lista):
    print(num * y)
