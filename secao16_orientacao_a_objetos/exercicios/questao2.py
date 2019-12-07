"""
2) Crie um classe Agenda que pode armazenar 10 pessoas e seja capas de
realizar as seguintes operações:

    . void armazenaPessoa(String nome, int idade, float altura);
    . void removePessoa(String nome);
    . int buscaPessoa(String nome);  // informa em que posição da agenda está a pessoa
    . void imprimeAgenda();  // imprime os dados de todas as pessoas da agenda
    . void imprimePessoa(int index);  // imprime os dados da pessoa que está na posição
                                         "i" da agenda

"""

from secao16_orientacao_a_objetos.exercicios.questao1 import Pessoa
from secao13_leitura_escrita_de_arquivos.exercicio.verificacao import verificar_texto


class Agenda:

    def __init__(self):
        """Construtor que inicia o atributo de instância que irá armazenar as pessoas"""
        self.__pessoas = []

    def armazena_pessoa(self, nome, idade, altura):
        """Armazena uma pessoa de acordo com as informações passadas por parâmetro"""
        self.__pessoas.append(Pessoa(nome, idade, altura))

    def remove_pessoa(self, nome):
        """Remove a pessoa de acordo com o nome passo por parâmetro"""

        if verificar_texto(nome):

            nova_lista = []

            removido = False

            for posicao in range(len(self.__pessoas)):

                if nome.strip().title() == self.__pessoas[posicao].get_nome():
                    removido = True

                else:
                    nova_lista.append(self.__pessoas[posicao])

            if not removido:
                print("\nNenhuma pessoa encontrada com esse nome")

            else:
                self.__pessoas = nova_lista

        else:
            print(f"\nNome inválido")

    def busca_pessoa(self, nome):
        """Retorna a posição onde se encontra a pessoa com o nome passado por parâmetro"""

        if verificar_texto(nome):

            for posicao in range(len(self.__pessoas)):

                if nome.strip().title() == self.__pessoas[posicao].get_nome():
                    return f"\n{posicao}"

            return "\nNenhuma pessoa encontrada com esse nome"

        return "\nNome inválido"

    def imprimi_agenda(self):
        """Imprimi na tela as informações de cada pessoa da agenda"""

        print()
        for pessoa in self.__pessoas:
            print(f"Nome: {pessoa.get_nome()}; Idade: {pessoa.get_idade()}; Altura: {pessoa.get_altura()}")

    def imprimi_pessoa(self, index):
        """Imprime na tela as informações da pessoa que se encontra no índice informado"""

        try:
            if not type(index) == bool and not type(index) == float:

                index = int(index)

                nome = self.__pessoas[index].get_nome()
                altura = self.__pessoas[index].get_altura()
                idade = self.__pessoas[index].get_idade()

                print(f"\nNome: {nome}; Idade: {idade}; Altura: {altura}")

            else:
                raise ValueError

        except ValueError:
            print("\nÍndice deve ser um inteiro")

        except TypeError:
            print("\nÍndice deve ser um inteiro")

        except IndexError:
            print("\nÍndice informado não existe")


if __name__ == "__main__":

    agenda = Agenda()

    agenda.armazena_pessoa("Pedro Henrique Gomes Lima", 21, 1.70)
    agenda.armazena_pessoa("Áquila Rodrigues Menezes", 23, 1.75)
    agenda.armazena_pessoa("Lucas Ravel Benicio Pinto", 21, 1.72)
    agenda.armazena_pessoa("Marcos Vitor Bezerra", 29, 1.85)
    agenda.armazena_pessoa("Rian Marlon Sousa da Silva", 25, 1.76)
    agenda.armazena_pessoa("Só o Básico", 80, 1.70)
    agenda.armazena_pessoa("Vitor Emanuel Sampaio Cavalcante", 29, 1.80)
    agenda.armazena_pessoa("Raffa Muela Mano", 49, 1.90)

    agenda.imprimi_agenda()

    agenda.remove_pessoa("Só o básico")

    agenda.imprimi_agenda()

    agenda.remove_pessoa("raffa muela mano")

    agenda.imprimi_agenda()

    print(agenda.busca_pessoa("vitor emanuel sampaio cavalcante"))
    agenda.imprimi_pessoa(5)
