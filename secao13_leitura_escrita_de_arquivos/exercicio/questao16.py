"""
16) Faça um programa que recebe um vetor de 10 números, converta
cada um desses números para binário e grave a sequência de 0s e 1s
em um arquivo texto. Cada número deve ser gravado em uma linha.
"""

vetor_numeros = ['10', 234, 7884, 9832, 332, 2299, 8873, 45, 3, 99]

try:

    if len(vetor_numeros) != 10:
        raise IndexError

    with open("arquivos/numeros_binarios.txt", "w") as arquivo:

        for numero in vetor_numeros:

            elemento = str(numero)
            num = int(elemento)

            binario = format(num, "b")

            arquivo.write(f"{binario}\n")

        print("\nInformações inseridas no arquivo com sucesso!")


except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO vetor deve conter apenas números!")

except IndexError:
    print("\nO vetor deve conter 10 elementos!")
