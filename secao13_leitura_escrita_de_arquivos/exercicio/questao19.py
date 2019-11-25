"""
19) Faça um programa que receba do usuário um arquivo que contenha o nome
e a nota de diversos alunos.txt (da seguinte forma: NOME:JOÃO NOTA:8), um aluno
por linha. Mostre na tela o nome e a nota do aluno que possui a maior nota.
"""

nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo+".txt"

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # strip() para remover os espaçoes e as quebras de linhas desnecessárias
        # do início e final do arquivo. splitlines() para criar um vetor
        # onde cada elemento é uma linha do arquivo
        linhas = arquivo.read().lower().strip().splitlines()

        # Removendo as partes do texto que contém "nome:" e "nota:"
        linhas = [linha.replace("nome:", "") for linha in linhas]
        linhas = [linha.replace("nota:", "") for linha in linhas]

        linhas = [linha.split() for linha in linhas]

        # Pegando o vetor que contém as informações do aluno com a maior nota
        aluno = max((linha for linha in linhas), key=lambda dados: float(dados[-1]))

        nome = aluno[0]
        nota = float(aluno[-1])

        print(f"\n{nome.title()} - {nota}")

except FileNotFoundError:
    print("\nArquivo não encotrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

