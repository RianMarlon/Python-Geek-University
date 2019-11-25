"""
23) Escreva um programa que leia a profissão e o tempo de serviço (em anos)
de cada um dos 5 funcionários de uma empresa e armazene-os no arquivo "emp.txt".
Cada linha do arquivo corresponde aos dados de um funcionário.
"""

from verificacao import verificar_texto

try:

    with open("arquivos/emp.txt", "w", encoding="utf-8") as arquivo:

        for i in range(5):

            profissao = str(input("Digite a profissão do funcionário: ")).strip().title()

            if verificar_texto(profissao):
                tempo_servico = abs(int(input("Digite o tempo de serviço do funcionário(em anos): ")))
                print()

                arquivo.write(f"{profissao} - {tempo_servico} anos\n")

            else:
                print("\nO nome da profissão não pode conter caracteres especiais ou números!")

    print("Informações inseridas no arquivo!")

except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO tempo de serviço deve ser um número inteiro!")
