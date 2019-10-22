"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)  # 1, 2, 3, 4

Se quiermos criar um set (conjunto)

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{chave:valor for valor in iterável}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

"""

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
