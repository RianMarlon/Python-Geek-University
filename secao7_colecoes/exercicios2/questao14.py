"""
14) Faça um prorgrama para gerar automaticamente números entre 0 e 99 de uma
cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5
números, gere estes dados de modo a não ter números repetidos dentro das cartelas.
O programa deve exibir na tela a cartela gerada.
"""

from random import randint

lista1 = []
lista3 = []

while len(lista1) < 5:

    lista2 = []
    while len(lista2) < 5:
        num = randint(0, 99)

        # Se o número aleatório não existir na lista3, adicione o valor na lista3 e adicione o valor na matriz lista2
        # Assim, o número não irá se repetir em nenhuma matriz
        if num not in lista3:
            lista3.append(num)

            lista2.append(num)

    lista1.append(lista2)

for i in range(5):

    for j in range(5):
        print(lista1[i][j], end='  ')

    print()
