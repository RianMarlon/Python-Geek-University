"""
3) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais.
"""


def conta_vogais(txt):
    """Retorna a quantidade de vogais que existe no texto recebido por parâmetro.
    Caso o que for passado por parâmetro não seja uma string, retornará um valor do tipo None"""

    try:
        vogais = ['a', 'e', 'i', 'o', 'u']

        txt = txt.lower()

        qtd = 0

        for vogal in vogais:
            qtd += txt.count(vogal)

        return qtd

    except AttributeError:
        return None


if __name__ == '__main__':

    nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                             "(caso o arquivo esteja no mesmo local do programa): "))

    nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            print(f"\nO arquivo texto tem {conta_vogais(texto)} vogais!")

    except FileNotFoundError:
        print("\nArquivo informado não encontrado!")

    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
