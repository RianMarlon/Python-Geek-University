"""
12) Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas
e o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais
caracteres espaços, tabulação ou nova linha.
"""

from questao6 import qtd_letras

nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        texto = arquivo.read()

        quebra_de_linha = texto.count("\n")

        caracteres = len(texto) - quebra_de_linha
        print(f"\nO arquivo tem {caracteres} caracter(es)!")

        print(f"O arquivo tem {quebra_de_linha+1} linha(s)!")

        palavras = texto.strip().split()

        print(f"O arquivo possui {len(palavras)} palavra(s)!")

        qtd_letras(texto)

except FileNotFoundError:
    print("\nArquivo informado não encontrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
