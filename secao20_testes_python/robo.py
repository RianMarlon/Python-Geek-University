

class Robo:

    def __init__(self, nome, bateria=100, habilidades = []):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f"BEEP BOOP BEEP BOOP... EU SOU {self.__nome.upper()}"

        return "Bateria fraca. Por favor, recarregue e tente novamente"

    def aprender_habilidade(self, nova_habilidade, custo):

        if self.__bateria >= custo:

            self.__bateria -= custo
            self.__habilidades.append(nova_habilidade)
            return f"UAU! EU APRENDI {nova_habilidade.upper()}"

        return "Bateria insuficiente. Por favor, recarregue e tente novamente"
