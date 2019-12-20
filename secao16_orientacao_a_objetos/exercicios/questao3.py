"""
3) Crie uma classe denominada Elevador para armazenar as informações de um
elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0),
total de andares no prédio, excluindo o térreo, capacidade do elevador, e
quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

    . Inicializa: que deve receber como parâmetros a capacidade do elevador e
    o total de andares no prédio (os elevadores sempre começam no térreo vazio);
    . Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
    houver espaço);
    . Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
    dentro dele);
    . Sobe: para subir um andar (não deve subir se já estiver no último andar);
    . Desce: para descer um andar (não deve descer se já estiver no térreo);
    . Encapsular métodos os atributs da classe (criar métodos set e get).

"""


class Elevador:

    def __init__(self, capacidade, total_andares):
        """Construtor que recebe a capacidade(int) do elevador e a quantidade
        de andares que contém o prédio(int)"""

        self.__andar = 0
        self.__quantidade_pessoas = 0

        try:

            if not type(capacidade) == bool and not type(total_andares) == bool:

                if not type(capacidade) == float and not type(total_andares) == float:

                    if int(capacidade) >= 0 and int(total_andares) > 0:

                        self.__capacidade = int(capacidade)
                        self.__total_andares = int(total_andares)

                    else:
                        raise ValueError

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    def get_andar(self):
        """Retorna o andar que o elevador se encontra"""
        return self.__andar

    def get_quantidade_pessoas(self):
        """Retorna a quantidade de pessoas do elevador"""
        return self.__quantidade_pessoas

    def get_capacidade(self):
        """Retorna a capacidade do elevador"""
        return self.__capacidade

    def get_total_andares(self):
        """Retorna a quantidade de andar(es) que tem/têm no prédio"""
        return self.__total_andares

    def set_capacidade(self, nova_capacidade):
        """Recebe um valor do tipo int que será o novo valor do atributo
         de instância 'capacidade'"""
        try:
            if not type(nova_capacidade) == bool and not type(nova_capacidade) == float:

                if int(nova_capacidade) >= 0 and int(nova_capacidade) >= self.__quantidade_pessoas:
                    self.__capacidade = int(nova_capacidade)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nCapacidade inválida")

    def set_total_andares(self, novo_total_andares):
        """Recebe um valor do tipo int que será o novo valor do atributo
        de instância 'total_andares'"""
        try:
            if not type(novo_total_andares) == bool and not type(novo_total_andares) == float:

                if int(novo_total_andares) >= 0 and novo_total_andares >= self.__andar:
                    self.__total_andares = int(novo_total_andares)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nTotal de andares inválido")

    def entra(self):
        """Adiciona 1 pessoa no atributo de instância 'pessoas'"""

        if self.__quantidade_pessoas < self.__capacidade:
            self.__quantidade_pessoas += 1

        else:
            print("\nO Elevador não tem capacidade para essa quantidade de pessoas")

    def sai(self):
        """Retira 1 pessoa do tributo de instância 'pessoa'"""

        if self.__quantidade_pessoas > 0:
            self.__quantidade_pessoas -= 1

        else:
            print("\nNão há ninguém no elevador")

    def sobe(self):
        """Retira 1 pessoa do tributo de instância 'andar'"""

        if self.__andar < self.__capacidade:

            self.__andar += 1

        else:
            print(f"\nO elevador já se encontra no último andar")

    def desce(self):
        """Adiciona 1 pessoa no atributo de instância 'andar'"""

        if self.__andar > 0:

            self.__andar -= 1

        else:
            print(f"\nO elevador já se encontra no térreo")


if __name__ == "__main__":

    elevador1 = Elevador(9, 12)

    print(f"\nAndar do Elevador 1: {elevador1.get_andar()}")
    print(f"Capacidade do Elevador 1: {elevador1.get_capacidade()}")
    print(f"Quantidade de pessoas no Elevador 1: {elevador1.get_quantidade_pessoas()}")
    print(f"Total de andares do prédio onde se encontra o Elevador 1: {elevador1.get_total_andares()}")

    [elevador1.entra() for _ in range(5)]
    [elevador1.sai() for _ in range(2)]

    [elevador1.sobe() for _ in range(5)]
    [elevador1.desce() for _ in range(3)]

    print(f"\nAndar do Elevador 1: {elevador1.get_andar()}")
    print(f"Capacidade do Elevador 1: {elevador1.get_capacidade()}")
    print(f"Quantidade de pessoas no Elevador 1: {elevador1.get_quantidade_pessoas()}")
    print(f"Total de andares do prédio onde se encontra o Elevador 1: {elevador1.get_total_andares()}")

    elevador1.set_capacidade(9)
    elevador1.set_total_andares(11)

    print(f"\nAndar do Elevador 1: {elevador1.get_andar()}")
    print(f"Capacidade do Elevador 1: {elevador1.get_capacidade()}")
    print(f"Quantidade de pessoas no Elevador 1: {elevador1.get_quantidade_pessoas()}")
    print(f"Total de andares do prédio onde se encontra o Elevador 1: {elevador1.get_total_andares()}")

    elevador2 = Elevador(14, 18)

    [elevador2.entra() for _ in range(10)]
    [elevador2.sobe() for _ in range(14)]

    print(f"\nAndar do Elevador 2: {elevador2.get_andar()}")
    print(f"Capacidade do Elevador 2: {elevador2.get_capacidade()}")
    print(f"Quantidade de pessoas no Elevador 2: {elevador2.get_quantidade_pessoas()}")
    print(f"Total de andares do prédio onde se encontra o Elevador 2: {elevador2.get_total_andares()}")

