"""
7) Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo
texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'
"""


def substitui_vogais(txt):
    """Recebe um texto e retorna o mesmo com as vogais substituidas por '*'.
    Caso não seja passado um texto por parâmetro, retornará uma string vazia"""

    try:
        vogais = ['a', 'e', 'i', 'o', 'u']

        for vogal in vogais:

            txt = txt.replace(vogal.lower(), "*")
            txt = txt.replace(vogal.upper(), "*")

        return txt

    except AttributeError:
        return ""


if __name__ == "__main__":

    nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                             "(caso o arquivo esteja no mesmo local do programa): "))

    nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

            with open("arquivos/arq2.txt", "w", encoding="utf-8") as arquivo_novo:

                arquivo_novo.write(substitui_vogais(arquivo.read()))

        print("\nTexto inserido no arquivo com sucesso!")

    except FileNotFoundError:
        print("\nO arquivo não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
