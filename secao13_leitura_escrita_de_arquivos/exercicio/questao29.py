"""
29) Codifique um programa que manipule um arquivo contendo registros
descritos pelos seguntes campos: codigo_vendedor, nome_vendedor,
valor_da_venda e mes. A manipulação do arquivo em questão é feita
através da execução das operações disonibilizadas pelo seguinte menu:

    . Criar o arquivo de dados;
    . Incluir um determinado registro no arquivo;
    . Excluir um determinado vendedor no arquivo;
    . Alterar o valor de uma venda no arquivo;
    . Imprimir os registros na saída padrão;
    . Excluir o arquivo de dados;
    . Finalizar o programa.

Os registro devem estar ordenados no arquivo, de forma crescente, de acordo
com as informações contidas nos campos codigo_vendedor e mes. Não deve existir
mais de um registro no arquivo com mesmos valores nos campos codigo_vendedor e mes.
"""

from os import path, remove

from verificacao import verificar_nome


def criar_arquivo(arquivo):
    """Função que recebe o caminho/nome do arquivo que o usuário deseja criar
    e cria o mesmo"""

    try:

        with open(arquivo, "a") as _:
            pass

        print(f"\n\n{'-' * 53}INFORMAÇÕES{'-' * 53}")
        print("ARQUIVO CRIADO COM SUCESSO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)


def inserir_registro(arquivo):
    """Função que recebe o caminho/nome de um arquivo existente e
    insere um registro de acordo com os dados fornecidos pelo usuário. Caso
    o arquivo não exista, será impresso uma mensagem na tela informando ao usuário"""

    try:

        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:

            print(f"\n\n{'-' * 55}INSERIR{'-' * 55}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 117}")

            nome_vendedor = str(input("Insira o nome do vendedor: ")).strip().title()
            print(f"{'-' * 117}")

            if verificar_nome(nome_vendedor):

                valor_venda = abs(float(input("Insira o valor da venda: ")))
                print(f"{'-' * 117}")

                mes = abs(int(input("Insira o número referente ao mês da venda: ")))
                print(f"{'-' * 117}")

                if (mes >= 1) and (mes <= 12):

                    existe = False

                    with open(arquivo, "r", encoding="utf-8") as verificacao:

                        texto = verificacao.read().strip().splitlines()

                        texto = [informacoes.split(";") for informacoes in texto]

                        for linha in texto:

                            if codigo_vendedor == int(linha[0]) and mes == int(linha[3]):
                                existe = True

                    if not existe:

                        with open(arquivo, "a", encoding="utf-8") as insercao:
                            insercao.write(f"{codigo_vendedor};{nome_vendedor};{valor_venda};{mes}\n")

                        print(f"\n\n{'-' * 53}INFORMAÇÕES{'-' * 53}")
                        print("REGISTRO INSERIDOS COM SUCESSO!")
                        print("-" * 117)

                    else:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                        print("EXISTE UM REGISTRO COM OS MESMOS VALORES NO CÓDIGO DO VENDEDOR E MÊS DA VENDA!")
                        print("-" * 117)

                else:
                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                    print("MÊS INVÁLIDO!")
                    print("-" * 117)

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                print("O NOME DO VENDEDOR NÃO PODE CONTER CARACTERES ESPECIAIS OU NÚMEROS!")
                print("-" * 117)

        else:
            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 117)

    except ValueError:
        print(f"{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def excluir_vendedor(arquivo):
    """Função que recebe o caminho/nome do arquivo e de acordo com
    os dados fornecidos pelo usuário, deleta o vendedor do arquivo.
    Caso o arquivo não exista, será impresso uma mensagem na tela informando ao usuário"""

    try:

        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:

            print(f"\n\n{'-' * 55}EXCLUIR{'-' * 55}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 117}")

            with open(arquivo, "r", encoding="utf-8") as leitura:

                texto = leitura.read().strip().splitlines()

                texto = [informacoes.split(";") for informacoes in texto]

                conteudo = ""
                existe = False

                for linha in texto:

                    if codigo_vendedor == int(linha[0]):
                        existe = True

                    else:
                        cod, nome, venda, mes = linha[0], linha[1], linha[2], linha[3]

                        conteudo += f"{cod};{nome};{venda};{mes}\n"

                if existe:
                    with open(arquivo, "w", encoding="utf-8") as deletando:
                        deletando.write(conteudo)

                        print(f"\n\n{'-' * 53}INFORMAÇÕES{'-' * 53}")
                        print("VENDEDOR DELETADO COM SUCESSO!")
                        print("-" * 117)

                else:
                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                    print("O CÓDIGO DO VENDEDOR INFORMADO NÃO EXISTE!")
                    print("-" * 117)

        else:
            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 117)

    except ValueError:
        print(f"{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def alterar_venda(arquivo):
    """Função que recebe o caminho/nome do arquivo e de acordo com
    os dados fornecidos pelo usuário, altera o valor de determinada venda.
    Caso o arquivo não exista, será impresso uma mensagem na tela informando ao usuário"""

    try:

        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:

            print(f"\n\n{'-' * 51}ALTERAR VALOR{'-' * 52}")

            codigo_vendedor = abs(int(input("Insira o código do vendedor: ")))
            print(f"{'-' * 117}")

            cod_existe = False

            with open(arquivo, "r", encoding="utf-8") as verificacao:

                texto = verificacao.read().strip().splitlines()

                texto = [informacoes.split(";") for informacoes in texto]

                for linha in texto:

                    if codigo_vendedor == int(linha[0]):
                        cod_existe = True

                if cod_existe:

                    mes_venda = abs(int(input("Insira o número referente ao mês da venda: ")))
                    print(f"{'-' * 117}")

                    if (mes_venda >= 1) and (mes_venda <= 12):

                        mes_existe = False

                        for linha in texto:

                            if mes_venda == int(linha[3]):
                                mes_existe = True

                        if mes_existe:

                            novo_valor = abs(float(input("Insira o novo valor da venda: ")))
                            print(f"{'-' * 117}")

                            conteudo = ""

                            for linha in texto:

                                cod, nome, valor, mes = int(linha[0]), linha[1], float(linha[2]), int(linha[3])

                                if (codigo_vendedor == cod) and (mes_venda == mes):
                                    conteudo += f"{cod};{nome};{novo_valor};{mes}\n"

                                else:
                                    conteudo += f"{cod};{nome};{valor};{mes}\n"

                            with open(arquivo, "w", encoding="utf-8") as alterando:
                                alterando.write(conteudo)

                                print(f"\n\n{'-' * 53}INFORMAÇÕES{'-' * 53}")
                                print("VALOR ALTERADO COM SUCESSO!")
                                print("-" * 117)

                        else:
                            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                            print("O MÊS DA VENDA INFORMADO NÃO EXISTE!")
                            print("-" * 117)

                    else:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                        print("MÊS INVÁLIDO!")
                        print("-" * 117)

                else:
                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
                    print("CÓDIGO NÃO EXISTE!")
                    print("-" * 117)

        else:
            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 117)

    except ValueError:
        print(f"{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def imprimir_registros(arquivo):
    """Função que recebe o caminho/nome do arquivo e imprimi os registros.
    Caso o arquivo não exista, será impresso uma mensagem na tela informando ao usuário"""

    try:

        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:

            with open(arquivo, "r", encoding="utf-8") as leitura:
                print(f"\n\n{'-' * 54}REGISTRO{'-' * 55}")
                texto = leitura.read().strip().splitlines()

                if len(texto) > 0:
                    [print(f"{informacao.replace(';', ' - ')}\n{'-' * 117}") for informacao in texto]

                else:
                    print(f"\n{'-' * 117}")

        else:
            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def excluir_arquivo(arquivo):
    """Função que recebe o caminho/nome do arquivo e exclui o mesmo.
    Caso o arquivo não exista, será impresso uma mensagem na tela informando ao usuário"""

    try:

        arquivo_existe = path.exists(arquivo)

        if arquivo_existe:

            remove(arquivo)

            print(f"\n\n{'-' * 53}INFORMAÇÕES{'-' * 53}")
            print("ARQUIVO EXCLUÍDO COM SUCESSO!")
            print("-" * 117)

        else:
            print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
            print("O ARQUIVO NÃO EXISTE. PRIMEIRO CRIE O ARQUIVO!")
            print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


if __name__ == "__main__":

    nome_arquivo = "arquivos/vendedores.txt"

    try:

        while True:

            print(f"\n\n{'-' * 56}MENU{'-' * 57}")
            print("1 - Criar o arquivo de dados")
            print(f"{'-' * 117}")

            print("2 - Incluir um determinado registro no arquivo")
            print(f"{'-' * 117}")

            print("3 - Excluir um determinado vendedor no arquivo")
            print(f"{'-' * 117}")

            print("4 - Alterar o valor de uma venda no arquivo")
            print(f"{'-' * 117}")

            print("5 - Imprimir os registros na saída padrão")
            print(f"{'-' * 117}")

            print("6 - Excluir o arquivo de dados")
            print(f"{'-' * 117}")

            print("7 - Finalizar o programa")
            print(f"{'-' * 117}")

            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 117}")

            if opcao == 1:
                criar_arquivo(nome_arquivo)

            elif opcao == 2:
                inserir_registro(nome_arquivo)

            elif opcao == 3:
                excluir_vendedor(nome_arquivo)

            elif opcao == 4:
                alterar_venda(nome_arquivo)

            elif opcao == 5:
                imprimir_registros(nome_arquivo)

            elif opcao == 6:
                excluir_arquivo(nome_arquivo)

            elif opcao == 7:
                print(f"\n\n{'-' * 51}FIM DO PROGRAMA{'-' * 51}")
                break

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 117)
