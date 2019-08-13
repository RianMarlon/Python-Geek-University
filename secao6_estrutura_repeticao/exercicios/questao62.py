"""
62) Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro,
cinco, então há 2 + 4 + 4 + 6 + 5 = 21 letras usadas no total. Faça um programa
que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras.
OBS: Não conte espaços ou hífens
"""

unidades = ['um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove']

dezenas_10 = ['onze', 'doze', 'treze', 'cartoze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['dez', 'vinte', 'trinta', 'quarenta',
           'cinquenta', 'sessenta', 'setenta',
           'oitenta', 'noventa']

centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos',
            'quinhentos', 'seiscentos', 'setecentos',
            'oitocentos', 'novecentos']

cont = 0

for i in range(1, 1001):

    numero = str(i)

    # Números de apenas 1 dígito
    if len(numero) == 1:
        cont_unidade = int(numero[0])

        unidade = unidades[cont_unidade - 1]

        cont += len(unidade)

        print(unidades[cont_unidade - 1])

    # Números de 2 dígitos
    elif len(numero) == 2:
        if (int(numero) > 10) and (int(numero) < 20):
            cont_unidade = int(numero[1]) - 1

            dezena_10 = dezenas_10[cont_unidade]

            cont += len(dezena_10)

            print(dezenas_10[cont_unidade])

        else:
            if int(numero[1]) == 0:
                cont_dezena = int(numero[0])

                dezena = dezenas[cont_dezena - 1]

                cont += len(dezena)

                print(dezenas[cont_dezena - 1])

            else:
                cont_dezena = int(numero[0]) - 1

                cont_unidade = int(numero[1]) - 1

                dezena = dezenas[cont_dezena]

                unidade = unidades[cont_unidade]

                # + 1 Por causa da letra 'e'
                cont += len(unidade) + 1 + len(dezena)

                print(dezenas[cont_dezena] + ' e ' + unidades[cont_unidade])

    # Números de 3 dígitos
    elif len(numero) == 3:

        # Se número foi igual a 100
        if int(numero) == 100:
            cont += len('cem')
            print('cem')

        # Se o número for maior que 100 e possuir apenas centena e dezena
        elif int(numero[0]) >= 1 and int(numero[1]) >= 1 and int(numero[2]) == 0:
            cont_centena = int(numero[0]) - 1

            cont_dezena = int(numero[1]) - 1

            centena = centenas[cont_centena]

            dezena = dezenas[cont_dezena]

            # + 1 Por causa da letra 'e'
            cont += len(centena) + 1 + len(dezena)

            print(centenas[cont_centena] + ' e ' + dezenas[cont_dezena])

        # Se o número for maior que 100 e possuir apenas centena e unidade
        elif int(numero[0]) >= 1 and int(numero[1]) == 0 and int(numero[2]) >= 1:
            cont_centena = int(numero[0]) - 1

            cont_unidade = int(numero[2]) - 1

            centena = centenas[cont_centena]

            unidade = unidades[cont_unidade]

            # + 1 Por causa da letra 'e'
            cont += len(centena) + 1 + len(unidade)

            print(centenas[cont_centena] + ' e ' + unidades[cont_unidade])

        # Se o número for maior que 100 e possuir centena, dezena e unidade
        elif (int(numero[0]) >= 1) and (int(numero[1]) >= 1) and (int(numero[2]) >= 1):

            # Se possuir números entre 10 e 20, após a centena
            if (int(numero[0]) >= 1) and (int(numero[1]) == 1):
                cont_centena = int(numero[0]) - 1

                cont_dezena = int(numero[2]) - 1

                centena = centenas[cont_centena]

                dezena = dezenas_10[cont_dezena]

                # + 1 Por causa da letra 'e'
                cont += len(centena) + 1 + len(dezena)

                print(centenas[cont_centena] + ' e ' + dezenas_10[cont_dezena])

            else:
                cont_centena = int(numero[0]) - 1

                cont_dezena = int(numero[1]) - 1

                cont_unidade = int(numero[2]) - 1

                centena = centenas[cont_centena]

                dezena = dezenas[cont_dezena]

                unidade = unidades[cont_unidade]

                # + 2 Por causa da letra 'e' que se repetirá 2x
                cont += len(centena) + 1 + len(dezena) + 1 + len(unidade)

                print(centenas[cont_centena] + ' e ' + dezenas[cont_dezena] + ' e ' + unidades[cont_unidade])

    # Números de 4 dígitos
    elif len(numero) == 4:

        cont += len('mil')
        print('mil')

print()
print(f'Entre 1 e 1000 temos {cont} letras.')
