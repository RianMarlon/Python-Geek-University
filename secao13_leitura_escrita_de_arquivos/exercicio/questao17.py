"""
17) Faça um programa que leia um arquivo que contenha as dimensões de uma
matrix (linha e coluna), a quantidade de posições que serão anuladas, e as
posições a serem anuladas (linha e coluna). O programa lê esse arquivo e,
em seguida, produz um novo arquivo com a matriz com as dimensões dadas
no arquivo lido, e todas as posições especificadas no arquivo ZERADAS e o
restante recebendo o valor 1.
Ex: arquivo "matriz.txt"

3 3 2 /*3 e 3 dimensões da matriz e 2 posições que serão anuladas*/
1 0
1 2   /*Posições da matriz que serão anuladas.

arquivo "matriz_saida.txt"

saida:

1 1 1
0 1 0
1 1 1

"""

nome_arquivo = str(input("Digite o caminho do arquivo ou o seu nome "
                         "(caso o arquivo esteja no mesmo local do programa): "))

nome_arquivo = nome_arquivo if ".txt" in nome_arquivo else nome_arquivo+".txt"

try:

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:

        # Removendo as quebras de linhas e os espaços desnecessários
        # do início e final do arquivo e criando um vetor
        # onde cada elementos é uma linha do arquivo
        linhas = arquivo.read().strip().splitlines()

        # Criando uma matriz onde o elemento de cada vetor é um elemento de cada linha
        linhas = [linha.split() for linha in linhas]

        # A primeira linha deve fornecer 3 informações...
        if len(linhas[0]) != 3:
            raise IndexError

        # Verificando se a quantidade de posições que devem ser anuladas
        # é diferente da quantidade de linhas excluindo a primeira linha
        if int(linhas[0][2]) != len(linhas)-1:
            raise IndexError

        matriz = []

        # A quantidade de posições anuladas
        qtd_anuladas = int(linhas[0][2])

        # Criando a matriz e preenchendo as posições com o numero 1
        for i in range(int(linhas[0][0])):

            vetor = []

            for j in range(int(linhas[0][1])):
                vetor.append(1)

            matriz.append(vetor)

        # Colocando 0 nas posições informadas na segunda linha e adiante(do arquivo)
        for i in range(1, qtd_anuladas+1):

            vetor = linhas[i]

            matriz[int(vetor[0])][int(vetor[1])] = 0

        # Criando um novo arquivo para adicionar a matriz
        with open("arquivos/matriz_saida.txt", "w", encoding="utf-8") as novo_arquivo:

            for vetor in matriz:

                for elemento in vetor:

                    novo_arquivo.write(f"{elemento} ")

                novo_arquivo.write("\n")

        print("\nInformações inseridas no arquivo com sucesso!")


except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")

except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")

except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
