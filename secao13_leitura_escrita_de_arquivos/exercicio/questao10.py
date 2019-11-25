"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída.
O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa
seguida pelo seu número de habitantes.
"""

arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome "
                            "(caso o arquivo esteja no mesmo local do programa): "))

arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada + ".txt"

try:
    with open(arquivo_entrada, "r", encoding="utf-8") as arquivo1:

        with open("arquivos/cidade_populosa.txt", "w", encoding="utf-8") as arquivo2:
            linhas = arquivo1.read().strip().splitlines()

            populosa = max(linhas, key=lambda habitantes: int(habitantes[40::]))

            arquivo2.write(populosa)

    print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
