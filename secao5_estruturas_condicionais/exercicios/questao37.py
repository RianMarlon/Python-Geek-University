"""
37) As tarifas de certo parque de estacionamento são as seguintes:

    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
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

print()

# Validando a hora de chegada e a hora de saida
if (chegada_hora >= 0) and (chegada_hora < 24) and (partida_hora >= 0) and (partida_hora < 24):

    if (chegada_minuto >= 0) and (chegada_minuto < 60) and (partida_minuto >= 0) and (partida_minuto < 60):

        # Nesse caso ele passou apenas alguns minutos, então foi 1 hora arredondando
        if partida_hora == chegada_hora and partida_minuto > chegada_minuto:
            intervalo_hora += 1

        # Nesse caso aqui sempre será 23 horas e 1 ou mais minutos, então arredonda para 24
        elif partida_hora == chegada_hora and partida_minuto < chegada_minuto:
            intervalo_hora = 24

        elif partida_hora > chegada_hora:
            intervalo_hora = partida_hora - chegada_hora

            if chegada_minuto >= partida_minuto:
                pass

            else:
                intervalo_hora += 1

        else:
            intervalo_hora = 24 - (chegada_hora - partida_hora)

            if chegada_minuto >= partida_minuto:
                pass

            else:
                intervalo_hora += 1

    else:
        print("Minutos fora do intervalo de 0 à 59")

else:
    print("Hora fora do intervalo de 0 à 23")


# Quantidade que deve ser paga pela quantidade de horas passada no parque
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
