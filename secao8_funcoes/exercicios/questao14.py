"""
14) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:

    | CONSUMO    | (km/l)  | MENSAGEM
    | menor que  |   8     | Venda o carro!
    | entre      | 8 e 12  | Econômico
    | maior que  |  12     | Super econômico!
"""


def consumo_km_l(distancia, gasolina):
    """
    Função que recebe a distância percorrida por um carro e a quantidade da gasolina consumida
    por um carro, e imprimi uma mensagem de acordo com a quantidade de quilometros por litros usado
    :param distancia: Recebe a distância em quilometros percorrida pelo carro
    :param gasolina: Recebe a quantidade de gasolina em litros
    """

    consumo = distancia / gasolina

    print()
    if consumo < 8:
        print("Venda o carro!")

    elif (consumo >= 8) and (consumo <= 14):
        print("Econômico")

    elif consumo > 12:
        print("Super econômico!")


distan = float(input("Digite a distância em km: "))
gasoli = float(input("Digite o consumo da gasolina consumida pelo carro: "))

consumo_km_l(distan, gasoli)
