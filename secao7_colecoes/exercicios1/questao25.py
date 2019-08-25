"""
25) Faça um programa que preencha um vetor de tamanho 100
com os 100 primeiros naturais que não são múltiplos de 7 ou
que terminam com 7.
"""

vetor = []

for i in range(1, 100**5):

    if len(vetor) >= 100:
        break

    else:
        numero = str(i)

        if (not (i % 7 == 0)) or numero[len(numero)-1] == '7':
            vetor.append(i)

print(vetor)
