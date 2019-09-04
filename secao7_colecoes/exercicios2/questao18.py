"""
18) Faça um programa que permita ao usuário entrar com uma matriz de
3 x 3 números inteiros. Em seguida, gere um array unidemensional
pela soma dos números de cada coluna da matriz e mostrar na tela
esse array. Por exemplo, a matriz:

    5   -8    10
    1    2   15
    25  10   7

Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A primeira
posição será 5 + 1 + 25, e assim por diante:

   31  4  32
"""

lista = []
for i in range(3):

    lista2 = []
    for j in range(3):
        numero = int(input("Digite um número: "))
        lista2.append(numero)

    lista.append(lista2)

print()

somador = []
for i in range(3):

    soma = 0
    for j in range(3):
        print(lista[i][j], end='  ')
        soma += lista[j][i]

    somador.append(soma)

    print()

print()
for i in range(3):
    print(somador[i], end='  ')

print()
