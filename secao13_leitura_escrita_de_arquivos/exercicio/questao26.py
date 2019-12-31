"""
26) Crue um programa que declare uma classe para o cadastro de alunos.

    (a) Deverão ser armazenados, para cada aluno: matrícula, sobrenome (apenas um),
    e ano de nascimento.
    (b) Ao início do programa, o usuário deverá informar o número de alunos que
    serão armazenados
    (c) O programa deverá pedir ao usuário que entre com as informações dos alunos.
    (d) Em seguida, essas informações deverão ser gravadas em um arquivo

OBS: Como no curso ainda não foi abordado classes, então usarei o modo padrão

"""

from verificacao import verificar_data, verificar_nome


def inserir_alunos(arquivo):

    """Função que recebe o caminho/nome de arquivo e insere no mesmo
    os dados dos alunos fornecidos pelo usuário"""

    try:

        with open(arquivo, "a", encoding="utf-8") as insercao:

            matricula = abs(int(input("\nInsira a matrícula dos aluno: ")))

            existe = False

            with open(arquivo, "r", encoding="utf-8") as leitura:

                informacoes = leitura.read().strip().splitlines()
                informacoes = [infor.split(" - ") for infor in informacoes]

                for linha in informacoes:

                    if int(linha[0]) == matricula:
                        existe = True

            if not existe:

                sobrenome = str(input("Insira o sobrenome do aluno: ")).strip().title()

                if verificar_nome(sobrenome):

                    dd = abs(int(input("Insira o dia de nascimento do aluno: ")))
                    mm = abs(int(input("Insira o mês de nascimento do aluno: ")))
                    aaaa = abs(int(input("Insira o ano de nasicmento do aluno: ")))

                    data_valida = verificar_data(dd, mm, aaaa)

                    if data_valida:

                        dia = str(dd) if len(str(dd)) > 1 else "0"+str(dd)
                        mes = str(mm) if len(str(mm)) > 1 else "0" + str(mm)
                        ano = str(aaaa)

                        data = f"{dia}/{mes}/{ano}"

                        insercao.write(f"{matricula} - {sobrenome.split()[-1]} - {data}\n")

                    else:
                        print("\nA data de nascimento é inválida!")

                else:
                    print("\nO sobrenome é inválido!")

            else:
                print("\nA matrícula informada já existe!")

    except ValueError:
        print("\nOs valores informados são inválidos!")

    except FileNotFoundError:
        print("\nO programa não possui permissão para criar um diretório/pasta!")

    except OSError:
        print("\nO SO não aceita caracteres especiais em nomes de arquivos!")

    except IndexError:
        print("\nO modo que as informações se encontram no texto é inválido!")


if __name__ == '__main__':

    nome_arquivo = "arquivos/alunos_matriculas.txt"

    try:

        numero_alunos = abs(int(input("Digite o número de alunos: ")))

        for _ in range(numero_alunos):
            inserir_alunos(nome_arquivo)

    except ValueError:
        print("\nO valor informado é inválido!")