"""
24) Implemente um controle simples de mercadorias em umas despensa domésticas.
Para cada produto armazene um código numérico, descrição e quantidade atual.
O programa deve ter opções para entrada e retirada de produtos, bem como
um relatório geral e um de produtos não disponíveis. Armazene os dados
em arquivo binário.
"""


def inserir(arquivo):

    """Função que recebe o caminho/nome do arquivo e insere no arquivo os dados
    do produto informados pelo usuário. Caso o arquivo não exista o mesmo
    será criado"""

    try:

        with open(arquivo, "ab") as insercao:

            print(f"\n\n{'-' * 54}INSERÇÃO{'-' * 55}")

            cod = abs(int(input("Digite o código numérico do produto: ")))

            print("-" * 117)

            codigo_existe = False

            with open(arquivo, "rb") as leitura:

                informacoes = leitura.read().decode("utf8").strip().splitlines()
                informacoes = [infor.split(" - ") for infor in informacoes]

                for linha in informacoes:

                    if int(linha[0]) == cod:
                        codigo_existe = True

            if codigo_existe:

                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("CÓDIGO NUMÉRICO JÁ EXISTE!")

                print("-" * 117)

            else:
                descricao = str(input("Digite a descrição do produto: ")).strip()
                print("-" * 117)

                if descricao.strip() != "":

                    quantidade_atual = abs(int(input("Digite a quantidade atual do produto: ")))
                    print("-" * 117)

                    insercao.write(f"{cod} - {descricao} - {quantidade_atual}\n".encode("utf8"))

                    print(f"\n\n{'-' * 53}INFORMAÇÃO{'-' * 54}")

                    print("PRODUTO INSERIDO COM SUCESSO!")

                    print("-" * 117)

                else:

                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                    print("A DESCRIÇÃO NÃO PODE CONTER CARACTERES ESPECIAIS OU NÚMEROS!")

                    print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO RECEBER OS DADOS DO USUÁRIO OU AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def deletar(arquivo):

    """Função que recebe o caminho/nome do arquivo e deleta o produto do arquivo,
    de acordo com o código numérico do produto informado pelo usuário. Caso o arquivo
    não exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as conteudo:

            informacoes = conteudo.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:

                informacoes = [infor.split(" - ") for infor in informacoes]

                print(f"\n\n{'-' * 55}DELEÇÃ0{'-' * 55}")

                codigo = abs(int(input("Digite o código numérico do produto que você deseja deletar: ")))

                print("-" * 117)

                with open(arquivo, "wb") as delecao:

                    codigo_existe = False

                    for linha in informacoes:

                        if int(linha[0]) == codigo:
                            informacoes.remove(linha)
                            codigo_existe = True

                    for linha in informacoes:

                        delecao.write(f"{linha[0]} - {linha[1]} - {linha[2]}\n".encode("utf8"))

                    if codigo_existe:

                        print(f"\n\n{'-' * 53}INFORMAÇÃO{'-' * 54}")

                        print("PRODUTO DELETADO COM SUCESSO!")

                        print("-" * 117)

                    else:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                        print("CÓDIGO NUMÉRICO NÃO EXISTENTE!")

                        print("-" * 117)

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def retirar(arquivo):

    """Função que recebe o caminho/nome do arquivo e retira uma quantidade informada
    do produto, de acordo com os dados fornecidos pelo usuário. Caso o arquivo não exista o mesmo
    será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:

            informacoes = leitura.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:

                informacoes = [infor.split(" - ") for infor in informacoes]

                print(f"\n\n{'-' * 54}RETIRADA{'-' * 55}")

                codigo = abs(int(input("Digite o código numérico do produto que você deseja retirar: ")))

                print(f"{'-' * 117}")
                qtd_unidade = abs(int(input("Digite a quantidade que você deseja retirar desse produto: ")))

                print("-" * 117)

                with open(arquivo, "wb") as remocao:

                    codigo_existe = False

                    for linha in range(len(informacoes)):

                        if int(informacoes[linha][0]) == codigo:

                            codigo_existe = True

                            if int(informacoes[linha][2]) > 0:

                                if (int(informacoes[linha][2]) - qtd_unidade) >= 0:

                                    informacoes[linha][2] = str(int(informacoes[linha][2]) - qtd_unidade)
                                    print(f"\n\n{'-' * 53}INFORMAÇÃO{'-' * 54}")

                                    print("UNIDADES RETIRADAS COM SUCESSO!")

                                    print("-" * 117)

                                else:
                                    print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                                    print("NÃO PODE RETIRAR UMA QUANTIDADE MAIOR DO QUE A DISPONÍVEL NO ESTOQUE!")

                                    print(f"{'-' * 117}")

                            else:
                                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                                print("ACABOU O ESTOQUE DO PRODUTO INFORMADO!")

                                print(f"{'-' * 117}")

                    if not codigo_existe:
                        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                        print("CÓDIGO NUMÉRICO NÃO EXISTENTE!")

                        print("-" * 117)

                    for linha in informacoes:

                        remocao.write(f"{linha[0]} - {linha[1]} - {linha[2]}\n".encode("utf8"))

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


def relatorio(arquivo):

    """Função que recebe o caminho/nome do arquivo e imprimi na tela
     o conteúdo atual do arquivo. Caso o arquivo não exista o mesmo
    será criado"""

    try:
        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as leitura:
            print(f"\n\n{'-' * 51}RELATÓRIO GERAL{'-' * 51}")

            texto = leitura.read().decode("utf-8").strip().splitlines()

            if len(texto) > 0:

                [print(f"{informacoes}\n{'-' * 117}") for informacoes in texto]

            else:

                print(f"\n{'-' * 117}")

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)


def produtos_indisponiveis(arquivo):

    """Função que recebe o caminho/nome do arquivo e imprimi na tela
     a descrição dos produtos que estão com o estoque zerado. Caso o arquivo
    não exista o mesmo será criado"""

    try:

        with open(arquivo, "ab") as _:
            pass

        with open(arquivo, "rb") as indisponivel:

            informacoes = indisponivel.read().decode("utf8").strip().splitlines()

            if len(informacoes) > 0:

                informacoes = [infor.split(" - ") for infor in informacoes]

                indisponivel = False

                print(f"\n\n{'-' * 47}PRODUTOS INDISPONIVÉIS{'-' * 48}")

                for linha in range(len(informacoes)):

                    if int(informacoes[linha][2]) > 0:
                        pass

                    else:
                        indisponivel = True
                        print(informacoes[linha][1])
                        print(f"{'-' * 117}")

                if not indisponivel:
                    print(f"\n{'-' * 117}")

            else:
                print(f"\n\n{'-' * 56}ERRO{'-' * 57}")

                print("O ARQUIVO ESTÁ VAZIO!")

                print("-" * 117)

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("ERRO AO LER O ARQUIVO!")
        print("-" * 117)

    except FileNotFoundError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O PROGRAMA NÃO POSSUI PERMISSÃO PARA CRIAR UM DIRETÓRIO/PASTA!")
        print("-" * 117)

    except OSError:
        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O SO NÃO ACEITA CARACTERES ESPECIAIS EM NOMES DE ARQUIVOS!")
        print("-" * 117)

    except IndexError:
        print(f"\n{'-' * 117}")

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("O MODO QUE AS INFORMAÇÕES SE ENCONTRAM NO TEXO É INVÁLIDO!")
        print("-" * 117)


if __name__ == "__main__":

    nome_arquivo = "arquivos/mercadorias.bin"

    try:

        while True:

            print(f"\n\n{'-' * 56}MENU{'-' * 57}")
            print("1 - Inserir um produto")

            print(f"{'-' * 117}")
            print("2 - Deletar um produto")

            print(f"{'-' * 117}")
            print("3 - Remover unidades de produto")

            print(f"{'-' * 117}")
            print("4 - Relatório geral do arquivo")

            print(f"{'-' * 117}")
            print("5 - Produtos indisponivéis")

            print(f"{'-' * 117}")
            opcao = abs(int(input("\nDigite o número da opção que você deseja: ")))

            print(f"{'-' * 117}")

            if opcao == 1:

                inserir(nome_arquivo)

            elif opcao == 2:

                deletar(nome_arquivo)

            elif opcao == 3:

                retirar(nome_arquivo)

            elif opcao == 4:

                relatorio(nome_arquivo)

            elif opcao == 5:

                produtos_indisponiveis(nome_arquivo)

            else:
                print(f"\n\n{'-' * 51}FIM DO PROGRAMA{'-' * 51}")
                break

    except ValueError:
        print("-" * 117)

        print(f"\n\n{'-' * 56}ERRO{'-' * 57}")
        print("OPÇÃO INVÁLIDA!")
        print("-" * 117)
