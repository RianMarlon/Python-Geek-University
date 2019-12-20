"""
9) Escreva um código que apresente a classe Moto, com
atributos marca, modelo, cor e marcha e, o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O
atributos marcha indica em que a marcha a Moto se encontra no momento, sendo
representado de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.
"""

from secao13_leitura_escrita_de_arquivos.exercicio.verificacao import verificar_texto


class Veiculo:

    def __init__(self, marca, modelo, cor):
        """Construtor que recebe a marca, modelo e cor do veiculo, verificando
        se os mesmos são válidos ou não"""

        try:

            if type(marca) == str and type(modelo) == str and type(cor) == str:
                self.__marca = marca.strip().title()
                self.__modelo = modelo.strip().title()

                if verificar_texto(cor):
                    self.__cor = cor.strip().title()

                else:
                    print("\nCor inválida")

            else:
                raise ValueError

        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def marca(self):
        """Retorna o valor contido no atributo de instância 'marca'"""
        return self.__marca

    @property
    def modelo(self):
        """Retorna o valor contido no atributo de instância 'modelo'"""
        return self.__modelo

    @property
    def cor(self):
        """Retorna o valor contido no atributo de instância 'cor'"""
        return self.__cor

    @marca.setter
    def marca(self, nova_marca):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'marca'"""

        try:

            if type(nova_marca) == str:

                if self.__marca.strip() == "":
                    self.__marca = nova_marca.strip().title()

                else:
                    print("\nMarca já definida")

            else:
                raise ValueError

        except ValueError:
            print("\nMarca inválida")

    @modelo.setter
    def modelo(self, novo_modelo):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'modelo'"""

        try:

            if type(novo_modelo) == str:

                if self.__modelo.strip() == "":
                    self.__modelo = novo_modelo.strip().title()

                else:
                    print("\nModelo já definido")

            else:
                raise ValueError

        except ValueError:
            print("\nModelo inválido")

    @cor.setter
    def cor(self, nova_cor):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'cor'"""

        try:

            if type(nova_cor) == str and verificar_texto(nova_cor):

                if self.__cor.strip() == "":
                    self.__cor = nova_cor.strip().title()

                else:
                    print("\nCor já definida")

            else:
                raise ValueError

        except ValueError:
            print("\nCor inválida")

    def imprimir(self):
        """Método Abstrato"""
        raise NotImplementedError


class Moto(Veiculo):

    def __init__(self, marca, modelo, cor, marcha):
        """Construtor que recebe a marca, o modelo, a cor e a marcha da moto,
        chama a Classe Pai e verifica se os valores recebidos são válidos ou não"""
        super().__init__(marca, modelo, cor)

        try:

            if type(marcha) != bool:

                if int(marcha) >= 0:
                    self.__marcha = int(marcha)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")
            exit(1)

    @property
    def marcha(self):
        """Retorna o valor contido no atributo de instância 'marcha'"""
        return self.__marcha

    @marcha.setter
    def marcha(self, nova_marcha):
        """Recebe um valor que irá ser o novo valor do atributo de instância 'marcha'"""

        try:

            if type(nova_marcha) != bool:

                if int(nova_marcha) >= 0:
                    self.__marcha = int(nova_marcha)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nValor inválido")

    def imprimir(self):
        """Imprimi todos os valores de todos os atributos"""
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Marcha atual: {self.marcha}")


if __name__ == "__main__":
    moto1 = Moto("Yamaha", "Xj6", "Branco", 6)
    moto1.imprimir()

    moto2 = Moto("Kawasaki", "Ninja H2 Carbon", "Prata", 8)
    moto2.imprimir()

    moto3 = Moto("Kawasaki", "Ninja H2R", "Prata", 8)
    moto3.imprimir()

