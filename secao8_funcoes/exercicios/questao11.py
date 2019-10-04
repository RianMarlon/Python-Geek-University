"""
11) Elabore uma função que receba três notas de um aluno como parâmetros e
uma letra. Se a letra for A, a função deverá calcular a média aritmética das
notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3, e 2.
"""


def calculo(nota1, nota2, nota3, letra='A'):
    """
    Função que recebe três notas de um aluno, uma letra(opcional, que por padrão é 'A', mas que pode ser 'P')
    e retorna uma mensagem informando o valor da média desejada
    :param nota1: Recebe a primeira nota do aluno
    :param nota2: Recebe a segundo nota do aluno
    :param nota3: Recebe a terceira nota do aluno
    :param letra: Recebe uma letra que indicará o calculo que deve ser realizado(opcional)
    :return: Retorna uma mensagem com o valor da média desejada. Se a letra for inválida
    retorna uma mensagem informando que a letra é inválida
    """

    if str(letra).upper() == 'A':
        media_aritmetica = (nota1+nota2+nota3) / 3
        return "Média aritmetica do aluno: %.1f" % media_aritmetica

    elif str(letra).upper() == 'P':
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return "Média ponderada do aluno: %.1f" % media_ponderada

    return 'Letra inválida'


not1 = float(input("Digite a primeira nota do aluno: "))
not2 = float(input("Digite a segunda nota do aluno: "))
not3 = float(input("Digite a terceira nota do aluno: "))

letr = str(input("Digite a letra referente ao calculo: "))

print(f"\n{calculo(not1, not2, not3, letr)}")
