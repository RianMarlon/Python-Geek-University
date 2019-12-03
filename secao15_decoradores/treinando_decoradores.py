

from functools import wraps


def chat_bot(funcao):
    """Recebe uma função que é responsável pela fala do bot"""

    @wraps(funcao)
    def fala(*args, **kwargs):
        """Recebe os parâmetros(caso exista) da função recebida por parâmetro"""
        print("\nMeu nome é Gary O Bot '.'\n".upper())
        print(funcao(*args, **kwargs))

        if "?" in funcao(*args, **kwargs):
            input()

        print("\nATENDIMENTO VIRTUAL\n")

    return fala


@chat_bot
def recepcao(nome):
    """Recebe o nome do usuário por parâmetro"""
    return f"Olá {nome.title().strip()}, como você está? O que posso fazer para ajudá-lo?"


@chat_bot
def demonstracao_produtos(*args):
    """Recebe os produtos e mostra ao cliente"""
    return f"Essa é a nossa lista de produtos: {', '.join(args)}"


@chat_bot
def nao_compreendido(nome):
    """Informa que não entendeu o que o usuário pediu"""
    return f"Desculpa {nome}, não entendi o que você deseja. Pode ser mais objetivo? Por favor."


@chat_bot
def satisfacao(nome):
    """Recebe o nome do cliente e faz algumas perguntas"""
    return f"{nome} você está satisfeito com o nosso atendimento? O que podemos fazer para melhorar?"


@chat_bot
def despedida(nome):
    """Recebe o nome do cliente e se despede do mesmo"""
    return f"Foi um prazer conhecê-lo {nome.title().strip()}. Até mais, espero vê-lo novamente por aqui!"


# recepcao("Rian Marlon")
# demonstracao_produtos("Notebook Dell Gaming com RTX 2060", "Mouse Gamer Logitech G403",
#                       "Teclado Gamer Razer", "Playstation 4 Slim", "Xbox One X")
# satisfacao("Rian Marlon")
# despedida("Rian Marlon")
#
#
# print(f"Função: {despedida.__name__}")
# print(f"Documentação: {despedida.__doc__}")


def forcar_tipo(*tipos):

    def forcando(funcao):

        @wraps(funcao)
        def finalizando(*args, **kwargs):

            print(f"\nVocê está usando a função: {funcao.__name__}")
            print(f"A documentação da função {funcao.__name__}: {funcao.__doc__}\n")

            numeros = []

            try:

                for (tipo, infor) in zip(tipos, args):
                    numeros.append(tipo(infor))

                return funcao(*numeros, **kwargs)

            except ValueError:
                return None

        return finalizando

    return forcando


@forcar_tipo(float, float)
def soma(num1, num2):
    """Soma dois números"""
    print(num1 + num2)


@forcar_tipo(float, float)
def multiplicacao(num1, num2):
    """Multiplica dois números"""
    print(num1 * num2)


@forcar_tipo(float, float)
def divisao(num1, num2):
    """Divisão de um número por outro"""
    print(num1 / num2)


soma("43", "8789.990")
multiplicacao("43", "8789.990")



