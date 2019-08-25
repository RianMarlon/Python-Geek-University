"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem
valores iguais e os escreva na tela.
"""

lista = []
verifica = []

for i in range(10):
    lista.append(int(input("Digite um valor: ")))

    if lista[i] in verifica:
        print(f"Já existe o valor {lista[i]} no vetor")

    verifica.append(lista[i])

print(verifica)