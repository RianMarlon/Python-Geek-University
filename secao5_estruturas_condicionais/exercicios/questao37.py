"""
37) As tarifas de certo parque de estacionamento são as seguintes:

    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacioanr durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
sao apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12,50 representará 'dez para a uma da parte'. Pretende-se
criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva
na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada
for supeiror à da partida, isso não é uma situação de erro, antes siginificará que
a partida ocorreu no dia seguinte ao chegada.
"""

chegada_hora = int(input("Digite a hora de chegada: "))
chegada_minuto = int(input("Digite o minuto da chegada: "))

print()
partida_hora = int(input("Digite a hora de partida: "))
partida_minuto = int(input("Digite o minuto da partida: "))

intervalo_hora = 0
intervalo_minuto = 0

print()
if (chegada_hora >= 0) and (chegada_hora < 24) and (partida_hora >= 0) and (partida_hora < 24):

    if partida_hora < chegada_hora:

        intervalo_hora = 24 + (partida_hora - chegada_hora)
        if (chegada_minuto >= 0) and (chegada_minuto < 60) and (partida_minuto >= 0) and (partida_minuto < 60):

            if chegada_minuto >= partida_minuto:
                intervalo_minuto = chegada_minuto - partida_minuto

                if intervalo_minuto > 0:
                    intervalo_hora += 1
                    intervalo_minuto = 0

            else:
                intervalo_minuto = partida_minuto - chegada_minuto

                if intervalo_minuto > 0:
                    intervalo_hora += 1
                    intervalo_minuto = 0

        else:
            print("Minutos fora do intervalo de 0 - 59")

    else:
        intervalo_hora = partida_hora - chegada_hora
        if (chegada_minuto >= 0) and (chegada_minuto < 60) and (partida_minuto >= 0) and (partida_minuto < 60):

            if chegada_minuto >= partida_minuto:
                intervalo_minuto = chegada_minuto - partida_minuto

                if intervalo_minuto > 0:
                    intervalo_hora += 1
                    intervalo_minuto = 0

            else:
                intervalo_minuto = partida_minuto - chegada_minuto

                if intervalo_minuto > 0:
                    intervalo_hora += 1
                    intervalo_minuto = 0

        else:
            print("Minuto fora do intervalo de 0 à 59")

else:
    print("Hora fora do intervalo de 0 à 23")


if intervalo_hora > 0:

    print(f"Tempo permanecido no estacionamento: {intervalo_hora} horas ")

    if (intervalo_hora >= 1) and (intervalo_hora <= 2):
        print("Deve pagar R$1,00")

    elif (intervalo_hora >= 3) and (intervalo_hora <= 4):
        print("Deve pagar R$1,40")

    elif intervalo_hora > 5:
        print("Deve pagar R$2,00")

    else:
        print("Erro")

else:
    print("A hora passada no estacionamento não pode ser 0")