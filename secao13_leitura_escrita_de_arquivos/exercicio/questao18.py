"""
18) Faça um programa que leia um arquivo contendo o nome e o preço de diversos
produtos (separados por linha), e calcule o total da compra.
"""

nome_arquivo = str(input("Digite o caminho do arquivo ou seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo+".txt"

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.read().lower().strip().splitlines()

        valor_total = 0.0

        for linha in range(len(linhas)):

            if linha % 2 == 1:

                preco = linhas[linha].replace(",", ".") if "," in linhas[linha] else linhas[linha]

                preco = float(preco)

                valor_total += abs(preco)

        print("\nO valor total da compra: {:.2f}".format(valor_total))

except FileNotFoundError:
    print("\nArquivo não encontrado!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
