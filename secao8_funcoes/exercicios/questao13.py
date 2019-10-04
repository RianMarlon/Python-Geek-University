"""
13) Faça uma função que receba dois valores numéricos e um símbolo.
Este símbolo representará a operação que se deseja efetuar com os
números. Se o símbolo for + deverá ser realizada uma adição, se for -
uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.

"""


def calculadora(numero1, numero2, simbolo='+'):
    """
    Função que recebe dois número e um simbolo(opcional, que por padrão é '+',
    mas que pode ser '-', '*' ou '/'), e retorna o resultado do calculo de acordo com o simbolo recebido
    :param numero1: Recebe um número
    :param numero2: Recebe um número
    :param simbolo: Recebe um símbolo da operação matemática
    :return: Retorna uma mensagem com o valor do calculo quando o simbolo é válido,
    mas quando é inválido retorna uma mensagem informando que o simbolo é inválido
    """

    if simbolo == '+':
        soma = numero1 + numero2
        return f"{numero1} + {numero2} = {soma}"

    elif simbolo == '-':
        subtracao = numero1 - numero2
        return f"{numero1} - {numero2} = {subtracao}"

    elif simbolo == '*':
        multiplicao = numero1 * numero2
        return f"{numero1} * {numero2} = {multiplicao}"

    elif simbolo == '/':
        divisao = numero1 / numero2
        return f"{numero1} / {numero2} = {divisao}"

    return "Símbolo inválido"


num1 = int(input("Digite um número: "))
simb = str(input("Diite o simbolo da operação: "))
num2 = int(input("Digite um número: "))


print(f"\n{calculadora(num1, num2, simb)}")
