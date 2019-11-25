"""
14) Dado um arquivo contendo um conjunto de nome e data nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo
e a data de hoje e construa outro arquivo contendo o nome e a idade de cada
pessoa do primeiro arquivo.
"""

from datetime import date

nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        informacoes = arquivo.read()

        # O strip() irá remover coisas desnecessárias do inicio e fim do texto
        # o splitlines() criará um vetor, onde cada elemento do vetor é uma linha do arquivo
        informacoes = informacoes.strip().splitlines()

        # Irá criar outro vetor dentro de cada elemento(uma matriz),
        # separando a parte do nome e da data de nascimento
        informacoes = [informacao.split(";") for informacao in informacoes]

        # Um vetor para receber todos os nomes
        nomes = [infor[0] for infor in informacoes]

        # Criará uma matriz, onde o vetor de cada elemento separará o dia, mês e ano
        datas = [infor[1].split(" ") for infor in informacoes]

        # Colocando a data atual em uma variável
        data_hoje = date.today()
        ano_hoje = data_hoje.year
        mes_hoje = data_hoje.month
        dia_hoje = data_hoje.day

        with open("arquivos/nome_idade.txt", "w", encoding="utf-8") as novo_arquivo:
            for posicao in range(len(datas)):

                # O ano atual subtraido pelo ano da data de nascimento
                idade = ano_hoje - int(datas[posicao][2])

                if idade > 0:

                    # Se o mês da data de nascimento for maior que o mês atual...
                    if int(datas[posicao][1]) > mes_hoje:
                        idade -= 1

                    # Se o mês da data de nascimento for igual o mês atual e o dia da data de nascimento
                    # for maior que o dia atual...
                    elif int(datas[posicao][1]) == mes_hoje and int(datas[posicao][0]) > dia_hoje:
                        idade -= 1

                    novo_arquivo.write(f"Nome: {nomes[posicao]};Idade: {idade}\n")

                else:
                    novo_arquivo.write(f"Nome: {nomes[posicao]};Idade: 0\n")

    print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
