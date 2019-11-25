"""
22) Faça um programa que recebe como entrada o nome de um arquivo de
entrada e o nome de um arquivo saída. O arquivo de entrada contém
o nome de um aluno ocupando 40 caracteres e três inteiros que indicam
suas notas. O programa deverá ler o arquivo de entrada e gerar um arquivo
de saída onde aparece o nome do aluno e as suas notas em ordem crescente.
"""


arquivo_entrada = str(input("Digite o caminho do arquivo de entrada ou o seu nome "
                            "(caso o arquivo esteja no mesmo local do programa): "))

arquivo_entrada = arquivo_entrada if ".txt" in arquivo_entrada else arquivo_entrada+".txt"

try:

    with open(arquivo_entrada, "r", encoding="utf-8") as entrada:

        arquivo_saida = str(input("Digite o caminho ou o nome do arquivo que você deseja criar: "))

        arquivo_saida = arquivo_saida if ".txt" in arquivo_saida else arquivo_saida + ".txt"

        conteudo = entrada.read()

        conteudo = conteudo.splitlines()

        informacoes = []

        for linha in conteudo:

            nome = linha[0:40:1]

            notas = linha[41::].split()

            notas = [int(notas[0].strip()), int(notas[1].strip()), int(notas[2].strip())]

            notas_crescente = sorted(notas, reverse=False)

            informacoes.append([nome, int(notas_crescente[0]), int(notas_crescente[1]), int(notas_crescente[2])])

        with open(arquivo_saida, "w", encoding="utf-8") as saida:

            for linhas in informacoes:

                saida.write(f"{linhas[0]} {linhas[1]} {linhas[2]} {linhas[3]}\n")

        print("\nInformações inseridas no arquivo com sucesso!")

except FileNotFoundError:
    print("\nO arquivo não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
