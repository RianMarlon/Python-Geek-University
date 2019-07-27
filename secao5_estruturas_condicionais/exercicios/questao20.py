"""
20) Dados três valores A, B, C, verificar se eles podem ser valores
dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimemiro de cada lado de um triângulo é menor
do que a soma dos outros dois lados.
    - Chama-se equilátero o triângulo que tem três lados iguais
    - Denominam-se isósceles o triângulo que tem o comprimento
de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

a = float(input("Digite o valor de A do triângulo: "))
b = float(input("Digite o valor de B do triângulo: "))
c = float(input("Digite o avlor de C do triângulo: "))

print()

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if (a == b) and (a == c):
        print("Triângulo equilátero!")

    elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
        print("Triâgulo isóscele!")

    elif (a != b) and (a != c) and (b != c):
        print("Triângulo escaleno!")

    else:
        print("Erro")

else:
    print("Não é umm triângulo")
