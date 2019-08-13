"""
33) Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos
de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída
deverá ser: 0,2,3,4,6,8.
"""
n = int(input("Digite o valor de n: "))

print()

if n > 0:
    valor1 = int(input("Digite o primeiro número: "))
    valor2 = int(input("Digite o segundo número: "))

    print()
    if valor1 > 0 and valor2 > 0:
        lista = []

        print(f"Os n primeiros naturais que são múltiplos de {valor1} ou de {valor2} e ou de ambos:")

        for i in range(n):
            if not (valor1 * i in lista):
                lista.append(valor1 * i)

            if not (valor2 * i in lista):
                lista.append(valor2 * i)

        lista.sort()

        for i in range(n):
            print(lista[i])

    else:
        print("Os número não podem ser zero ou negativo")

else:
    print("O valor de n não pode ser zero ou negativo")
