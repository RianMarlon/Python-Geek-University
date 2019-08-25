"""
34) Faça um programa para ler 10 números DIFERENTES a serem armazenados
em um vetor. Os dados deverão ser armazenados no vetor na ordem que
forem sendo lidos, sendo que o caso o usuário digite um número
que já foi digitado anteriormente, o programa deverá pedir para ele
digitar outro número. Note que cada valor digitado pelo usuário deve
ser pesquisado no vetor, verificando se ele existe entre os números que
já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""

lista = []

while True:

    if len(lista) >= 10:
        break

    num = int(input("Digite um número: "))

    if num in lista:
        print("Digite outro número")

    else:
        lista.append(num)

print(f"\nVetor final: {lista}")
