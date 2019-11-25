"""
6) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.
"""


def qtd_letras(txt):
    """Recebe um texto e imprimi na tela cada letra do alfabeto e a quantidade
    de vezes que a mesma aparece no texto. Caso não seja passado um texto, a função
    imprimirá uma mensagem informando que o valor recebido por parâmetro não é um texto"""

    txt = txt.lower()

    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print()

    try:
        for letra in letras:
            print(f"A letra {letra} se repete {txt.count(letra)} vezes no texto")

    except AttributeError:
        print("O valor recebido por parâmetro não é um texto/string")


if __name__ == "__main__":
    nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                             "(caso o arquivo esteja no mesmo local que do arquivo): "))

    nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo + ".txt"

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            texto = arquivo.read().lower()

            qtd_letras(texto)

    except FileNotFoundError:
        print("\nArquivo informado não encontrado!")

    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
