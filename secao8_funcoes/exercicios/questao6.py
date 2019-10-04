"""
6) Faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos
"""


def transformar_em_segundos(horas, minutos, segundos):
    """
    Função que recebe as horas, os minutos e segundos e retorna o resultado da conversão em segundos
    :param horas: recebe as horas
    :param minutos: recebe os minutos
    :param segundos: recebe os segundos
    :return: retorna o resultado da conversão em segundos de 'horas', 'minutos' e 'segundos'.
    Caso exista algum valor que não seja inteiro, retorna um valor do tipo None
    """

    if horas // 1 == horas:
        if minutos // 1 == minutos:
            if segundos // 1 == segundos:

                convertido = horas * 60 * 60
                convertido += minutos * 60
                convertido += segundos

                return convertido


horas1 = int(input("Digite as horas: "))
minutos1 = int(input("Digite os minutos: "))
segundos1 = int(input("Digite os segundos: "))

print(f"\nConvertido em segundos: {transformar_em_segundos(horas1, minutos1, segundos1)}")
