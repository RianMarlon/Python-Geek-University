"""
18) Faça uma função que receba por parâmero dois valores X e Z.
Calcule e retorne o resultado de X elevado a Z para o programa principal.
Atenção não utilize nenhuma função pronta de exponenciação.
"""


def exponenciacao(numero, expoente):
    """
    Função que recebe um número e um expoente. Retorna o resultado
    da variavel 'numero' elevado a 'expoente'
    :param numero: Recebe um valor
    :param expoente: Recebe um valor
    :return: Retorna o resultado do 'numero' elevado a 'expoente'
    """

    return numero ** expoente


num = int(input("Digite um número: "))
exp = int(input("Digite o expoente do número: "))

print(f"\n{num} ** {exp} = {exponenciacao(num, exp)}")
