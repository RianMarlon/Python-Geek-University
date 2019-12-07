"""
4) Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o
volume e trocar os canais da televisão.

    . O controle de volume permite aumentar ou diminuir a potência do volume
    de som em uma unidade de cada vez;
    . O controle de canal tambpem permite aumentar e diminuir o número do canal em
    uma unidade, porém, também possibilita trocar para um canal indicado;
    . Também devem existir métodos para consultar o valor do volume de som e o
    canal selecionado.

"""


class Televisao:

    def __init__(self, quantidade_canais):
        """Construtor que recebe a quantidade de canais(int)"""

        self.__volume = 0
        self.__canal = 1

        try:

            if not type(quantidade_canais) == bool and not type(quantidade_canais) == float:

                if int(quantidade_canais) > 0:

                    self.__quantidade_canais = int(quantidade_canais)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nQuantidade de canais é inválido")
            exit(1)

    def get_volume(self):
        """Retorna o volume que se encontra na Televisão"""
        return self.__volume

    def get_canal(self):
        """Retorna o canal que se encontra na Televisão"""
        return self.__canal

    def get_quantidade_canais(self):
        """Retorna a quantidade de canais que contém na Televisão"""
        return self.__quantidade_canais

    def set_volume(self, novo_volume):
        """Recebe um valor do tipo int que será o novo valor do atributo
        de instância 'volume'"""
        try:
            if not type(novo_volume) == bool and not type(novo_volume) == float:

                if (int(novo_volume) > 0) and (int(novo_volume) <= 100):
                    self.__volume = int(novo_volume)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nVolume fora do limite entre 0 e 100")

    def set_canal(self, novo_canal):
        """Recebe um valor do tipo int que será o novo valor do atributo
        de instância 'canal'"""
        try:
            if not type(novo_canal) == bool and not type(novo_canal) == float:

                if (int(novo_canal) > 0) and (int(novo_canal) <= self.__quantidade_canais):
                    self.__canal = int(novo_canal)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nEsse canal não existe")

    def set_quantidade_canais(self, nova_quantidade_canais):
        """Recebe um valor do tipo int que será o novo valor do atributo
         de instância 'quantidade_canais'"""
        try:
            if not type(nova_quantidade_canais) == bool and not type(nova_quantidade_canais) == float:

                if int(nova_quantidade_canais) >= 0 and int(nova_quantidade_canais) >= self.__canal:
                    self.__quantidade_canais = int(nova_quantidade_canais)

                else:
                    raise ValueError

            else:
                raise ValueError

        except ValueError:
            print("\nQuantidade de canais é inválido")


class ControleRemoto:

    def __init__(self, televisao):
        """Construtor que recebe um objeto da classe Televisao"""
        if type(televisao) == Televisao:
            self.__televisao = televisao

        else:
            print("\nValor inválido")
            exit(1)

    def aumentar_volume(self):
        """Aumenta o volume da Televisão de 1 em 1"""
        volume = self.__televisao.get_volume() + 1
        self.__televisao.set_volume(volume)

    def diminuir_volume(self):
        """Diminui o volume da Televisão de 1 em 1"""
        volume = self.__televisao.get_volume() - 1
        self.__televisao.set_volume(volume)

    def mudar_canal(self, novo_canal):
        """Muda para o canal passado por parâmetro"""
        self.__televisao.set_canal(novo_canal)

    def incrementar1_canal(self):
        """Vai para o próximo canal da Televisão"""
        canal = self.__televisao.get_canal() + 1
        self.__televisao.set_canal(canal)

    def decrementar1_canal(self):
        """Volta para o canal anterior da Televisão"""
        canal = self.__televisao.get_canal() - 1
        self.__televisao.set_canal(canal)


if __name__ == "__main__":

    tv1 = Televisao(500)

    controle1 = ControleRemoto(tv1)

    [controle1.aumentar_volume() for _ in range(50)]

    controle1.mudar_canal(200)

    controle1.decrementar1_canal()
    controle1.decrementar1_canal()

    controle1.diminuir_volume()
    controle1.diminuir_volume()

    controle1.incrementar1_canal()

    volume = tv1.get_volume()
    canal = tv1.get_canal()

    print(f"\nA Televisão está no volume: {volume}")
    print(f"A Televisão está no canal: {canal}")

