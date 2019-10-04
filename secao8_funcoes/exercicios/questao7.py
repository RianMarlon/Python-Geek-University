"""
7) Faça uma função que receba uma temperatura en graus Celsius e retorne-a
convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""


def converte_em_fahrenheit(celsius):
    """
    Função que recebe uma temperatura em graus Celsius e retorna em graus Fahrenheit
    :param celsius: recebe os graus celsius
    :return: retorna o resultado da conversão de graus Celsius em Fahrenheit
    """
    return celsius * (9.0/5.0) + 32.0


celsius1 = float(input("Digite a temperatura em graus Celsius: "))

print(f"\nTemperatura em graus Fahrenheit: {converte_em_fahrenheit(celsius1)}°F")
