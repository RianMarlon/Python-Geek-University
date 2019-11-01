

def soma(numero1, numero2):
    """Função que retorna a soma do dois números recebidos por parâmetro"""

    try:
        return int(numero1) + int(numero2)

    except ValueError:
        return "Apenas valores que podem ser convetidos em números inteiros"


def colore_texto(texto, cor):
    """Função que retorna o texto colorido com a cor passado por argumento"""

    try:
        cor = cor.strip().lower()
        cores = {"vermelho": "\033[31m", "verde": "\033[32m", "amarelo": "\033[33m",
                 "azul": "\033[34m", "roxo": "\033[35m", "ciano": "\033[36m", "cinza": "\033[37m"}

        if cor in cores.keys():
            return f"{cores[cor]}{texto}\033[m"

        else:
            raise ValueError

    except AttributeError:
        return f"A função deve receber apenas valores do tipo string"

    except ValueError:
        return "Cor inválida"


def data_por_extenso(dia, mes, ano):
    """
    Função que recebe um dia, mês e ano e retorna a data por extenso caso a mesma seja válida
    """
    try:

        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        if mes == 1:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de janeiro de {ano}"

            else:
                return "Data inválida"

        elif mes == 2:

            # Verificando se o ano informado é um ano bissexto
            if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
                if (dia >= 1) and (dia <= 29):
                    return f"{dia} de fevereiro de {ano}"

                else:
                    return "Data inválida"

            else:
                if (dia >= 1) and (dia <= 28):
                    return f"{dia} de fevereiro de {ano}"

                else:
                    return "Data inválida"

        elif mes == 3:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de março de {ano}"

            else:
                return "Data inválida"

        elif mes == 4:
            if (dia >= 1) and (dia <= 30):
                return f"{dia} de abril de {ano}"

            else:
                return "Data inválida"

        elif mes == 5:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de maio de {ano}"

            else:
                return "Data inválida"

        elif mes == 6:
            if (dia >= 1) and (dia <= 30):
                return f"{dia} de junho de {ano}"

            else:
                return "Data inválida"

        elif mes == 7:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de julho de {ano}"

            else:
                return "Data inválida"

        elif mes == 8:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de agosto de {ano}"

            else:
                return "Data inválida"

        elif mes == 9:
            if (dia >= 1) and (dia <= 30):
                return f"{dia} de setembro de {ano}"

            else:
                return "Data inválida"

        elif mes == 10:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de outubro de {ano}"

            else:
                return "Data inválida"

        elif mes == 11:
            if (dia >= 1) and (dia <= 30):
                return f"{dia} de novembro de {ano}"

            else:
                return "Data inválida"

        elif mes == 12:
            if (dia >= 1) and (dia <= 31):
                return f"{dia} de dezembro de {ano}"

            else:
                return "Data inválida"

        else:
            return"Data inválida"

    except ValueError:
        return "Apenas valores inteiros devem ser passados por argumento"


if __name__ == '__main__':
    print(soma(455, 'erro'))
    print(colore_texto("Largatixa tem o rabo amarelo", "amarelo"))
    print(data_por_extenso(16, 60, 13))
    print(data_por_extenso(12, 6, 2012))
