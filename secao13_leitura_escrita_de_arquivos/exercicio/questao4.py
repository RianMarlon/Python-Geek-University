"""
4) Faça um programa que receba do usuário um arquivo texto e mostre na tela
quantas letras são vogais e quantas são consoantes
"""

from questao3 import conta_vogais


def conta_consoantes(txt):
    """Retorna a quantidade de consoantes que existe no texto recebido por parâmetro.
    Caso o que for recebido por parâmetro não seja uma string, retornará um valor do tipo None"""

    try:
        consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                      'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

        txt = txt.lower()

        qtd = 0

        for consoante in consoantes:
            qtd += txt.count(consoante)

        return qtd

    except AttributeError:
        return None


if __name__ == '__main__':

    nome_arquivo = str(input("Digite o caminho do arquivo ou o nome do arquivo "
                             "(caso o arquivo esteja no mesmo local do programa): "))

    nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            print(f"\nO arquivo texto tem {conta_vogais(texto)} vogais e {conta_consoantes(texto)} consoantes!")

    except FileNotFoundError:
        print("\nArquivo informado não encontrado!")

    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
