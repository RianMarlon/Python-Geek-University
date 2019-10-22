#
#
# def media(args):
#
#     return sum(args) / len(args)
#
#
# res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# dobro = [num * 2 for num in res]
# print(dobro)
#
# quadrado = [num ** 2 if num % 2 == 0 else num / 2 for num in res]
# print(quadrado)
#
# nomes = ['guidon', 'alexia', 'luks', 'predro', 'dandan']
# capitalizado = [print(nome.capitalize()) for nome in nomes]
#
# valores = [[23, 43, 342, 3123, 434], [3234, 434, 21, 3454, 45], [3231, 342, 344, 434]]
#
# media = [print(media(valor))for valor in valores]
#
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tabuleiro = [["X" if numero % 2 == 1 else "O" for numero in lista] for lista in matriz]
# print(tabuleiro)
#
# num = int(input("Digite um número: "))
#
# print("Par" if num % 2 == 0 else "Impar")
#
# print(num ** 2 if num % 2 == 0 else num ** 0.5)
#
#
# num = [float(input("Digite um número: ")) for i in range(6)]
#
# print(num)
#
# letras = ['a', 'b', 'c', 'd', 'e', 'f']
# valores = [23, 123, 12, True, 'Uiui', 354]
#
# dicionario = {letras[i]: valores[i] for i in range(len(letras)) if len(valores) >= len(letras)}
# print(dicionario)
#
# numeros = [1, 2, 3, 4, 4322, 54, 432, 2546, 322, 43]
#
# tipo = {numero: "Par" if numero % 2 == 0 else "Impar" for numero in numeros}
# print(tipo)
#
# nomes = ['Rian', 'Pedro', 'Guidon', 'Aquila', 'Isabele']
#
# [print(nome) for nome in sorted(nomes)]
#
# lista = [i for i in range(8)]
# print(lista)
#
# numeros = [21, 23, 21, 23, 323, 43, 43, 232, 3435]
#
# sem_repeticao = {num for num in numeros}
# print(sem_repeticao)

lista = [int(input("Digite um numero: ")) for i in range(8)]
pares = [num for num in lista if num % 2 == 0]
print(f"\nPossui {len(pares)} números pares")
