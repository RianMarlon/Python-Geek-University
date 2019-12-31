"""
1) Crie um novo pacote com o nome: heranca. Todas as (três) classes criadas abaixo
deverão ser salvas neste pacote.

2) Crie uma classe Equipamento com dois atributos privados.

3) Crie uma classe Computador com dois atributos sua escolha,
também privados. A classe Computador deverá herdar tudo da classe
Equipamento.

4) Crie os métodos de acesso e de modificação para todos os
atributos definidos em ambas as classes.

5) Crie uma classe TestaEquipamento, que deverá conter o método
main(), crie nela um objeto da classe Equipamento e instancie
os dois atributos que você declarou na classe Equipamento.
Crie tambpem um objeto da classe Computador, utilizando os dois
atributos declarados na rópria classe e os dois herdados da classe
Equipamento.

6) O método main() deve exibir as informações dos dois objetos criados.

7) Criar o método exibe() na classe Equipamento para mostrar os dados dessa classe

8) Reescreva o método exibe() na classe Computador, aproveitando o que já
está escrito na superclasse Equipamento
"""


class Equipamento:

    def __init__(self, funcao, preco):
        """Construtor que recebe as informações referente ao equipamento, a função
        e o preço"""

        try:

            if type(funcao) == str:

                if funcao.strip() != "":
                    self.__funcao = funcao

                else:
                    raise ValueError

            else:
                raise ValueError

            if type(preco) != bool:

                if float(preco) >= 0:
                    self.__preco = float(preco)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def funcao(self):
        """Retorna o valor contido no atributo de instância 'funcao'"""
        return self.__funcao

    @property
    def preco(self):
        """Retorna o valor contido no atributo de instância 'preco'"""
        return self.__preco

    @funcao.setter
    def funcao(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'funcao'"""

        try:

            if type(novo_valor) == str:

                if novo_valor.strip() != "":
                    self.__funcao = novo_valor

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nFunção inválida")

    @preco.setter
    def preco(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'preco'"""

        try:

            if type(novo_valor) != bool:

                if float(novo_valor) >= 0:
                    self.__preco = float(novo_valor)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nPreço inválido")

    def exibe(self):
        """Exibe todos os valores de todos os atributos"""
        print(f"\nFunção: {self.__funcao}")
        print(f"Preço: {self.__preco}")


class Computador(Equipamento):

    def __init__(self, funcao, preco, ligado, processador):
        """Construtor que recebe as informações referente a função,
        preço, se está ligado ou não, o processador do computador e
        chama a Classe Pai e verifica se o valor recebido é válido ou não"""
        super().__init__(funcao, preco)

        try:
            if type(ligado) == str:

                if ligado.strip().title() == "False" or ligado.strip() == "0":
                    self.__ligado = False

                elif ligado.strip().title() == "True" or ligado.strip() == "1":
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(ligado) == int:

                if ligado == 0:
                    self.__ligado = False

                elif ligado == 1:
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(ligado) == bool:
                self.__ligado = ligado

            else:
                raise ValueError

            if type(processador) == str:

                if processador.strip() != "":

                    self.__processador = processador.strip().title()

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def ligado(self):
        """Retorna o valor contido no atributo de instância 'ligado'"""
        return self.__ligado

    @property
    def processador(self):
        """Retorna o valor contido no atributo de instância 'processador'"""
        return self.__processador

    @ligado.setter
    def ligado(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'ligado'"""

        try:
            if type(novo_valor) == str:

                if novo_valor.strip().title() == "False" or novo_valor.strip() == "0":
                    self.__ligado = False

                elif novo_valor.strip().title() == "True" or novo_valor.strip() == "1":
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(novo_valor) == int:

                if novo_valor == 0:
                    self.__ligado = False

                elif novo_valor == 1:
                    self.__ligado = True

                else:
                    raise ValueError

            elif type(novo_valor) == bool:
                self.__ligado = novo_valor

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    @processador.setter
    def processador(self, novo_valor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'processador'"""
        try:
            if type(novo_valor) == str:

                if novo_valor.strip() != "":

                    self.__processador = novo_valor.strip().title()

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nProcessador inválido")

    def exibe(self):
        """Exibe todos os valores de todos os atributos"""
        print(f"\nFunção: {self.funcao}")
        print(f"Preço: {self.preco}")
        print(f"Ligado? {'Sim' if self.ligado else 'Não'}")
        print(f"Processador: {self.__processador}")


class TestaEquipamento:

    def __init__(self):
        """Construtor padrão"""
        pass

    @staticmethod
    def main():
        """Cria um objeto da classe Equimento e Computador e executa a função exibe()
        de cada um dos objetos"""

        equipamento = Equipamento("Uso para entreterimento e para uso profissional/escolar", 2800.00)

        funcao = equipamento.funcao
        preco = equipamento.preco

        computador = Computador(funcao, preco, True, "I5 de Nona Geração")

        print("\nINFORMAÇÕES REFERENTES AO EQUIPAMENTO CRIADO:")
        equipamento.exibe()

        print("\nINFORMAÇÕES REFERENTES AO COMPUTADOR:")
        computador.exibe()


if __name__ == "__main__":
    # equipamento1 = Equipamento(" ", 920.00)
    # equipamento1.exibe()

    equipamento2 = Equipamento("Ajudar na construção de casas", 180.50)
    equipamento2.exibe()

    equipamento2.funcao = ""
    equipamento2.preco = -2.54

    computador = Computador("Diversão, entreterimento e para fins de estudo e trabalho", 2900.90,
                            False, "I7 de Oitava Geração")

    computador.exibe()

    computador.funcao = " "
    computador.processador = " "

    teste1 = TestaEquipamento()
    teste1.main()



