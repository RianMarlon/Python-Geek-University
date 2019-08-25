"""
35) Faça um programa que leia dois números a e b (positivos menores
que 10000) e:

    . Crie um vetor onde cada posição é um algorismo do número. A primeira
    posição é o algarismo menos significativo;
    . Crie um vetor que seja a soma de a e b, mas faça faça-o usando
    apenas os vetores construídos anteriormente.

Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia
10 do resultado e some 1 à próxima posição.
"""

a = int(input("Digite um número: "))

if (a > 0) and (a < 10000):
    b = int(input("Digite um número: "))

    if (b > 0) and (b < 10000):

        algarismos1 = list(str(a))
        algarismos2 = list(str(b))

        tamanho1 = len(algarismos1)
        tamanho2 = len(algarismos2)

        lista1 = []
        lista2 = []

        lista1.append(int(algarismos1[tamanho1-1]))

        for i in range(int(tamanho1 - 1)):
            lista1.append(int(algarismos1[i]))

        lista2.append(int(algarismos2[tamanho2 - 1]))

        for i in range(int(tamanho2 - 1)):
            lista2.append(int(algarismos2[i]))

        soma = [0, 0, 0, 0, 0]

        for i in range(4):

            if len(lista1) > i and len(lista2) > i:

                soma[i] += (int(lista1[i] + lista2[i]))

                if soma[i] > 10:
                    soma[i] -= 10
                    soma[i+1] += 1

            if not(len(lista1) > i) and len(lista2) > i:
                soma[i] += int(lista2[i])

            if len(lista1) > i and not(len(lista2) > i):
                soma[i] += int(lista1[i])

        if len(lista1) >= len(lista2):
            while len(soma) > len(lista1):
                if soma[-1] == 0:
                    soma.pop()

                else:
                    break

        elif len(lista2) >= len(lista1):
            while len(soma) > len(lista2):
                if soma[-1] == 0:
                    soma.pop()

                else:
                    break

        print()
        print(f"Primeira lista: {lista1}")
        print(f"Segunda lista: {lista2}")
        print(f"Soma das listas: {soma}")

    else:
        print("Digite apenas números positivos e menor que 10000")

else:
    print("Digite apenas números positivos e menor que 10000")
