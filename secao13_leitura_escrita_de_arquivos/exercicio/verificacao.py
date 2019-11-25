

def verificar_texto(texto):
    """Função que recebe um nome e verifica se o mesmo é válido ou não.
    Caso o nome seja válido retorna True, caso contrário retorna False"""

    caracteres_invalidos = ["-", ":", "?", "/", ">", "<", "}", "{", "[", "]",
                            "+", "*", "@", "!", "%", "¨", ";", "´", "`", "^", "~",
                            "=", "(", ")", "&", "_", "$", "#", ","]

    try:

        for caractere in texto:

            if str(caractere).isnumeric() or str(caractere) in caracteres_invalidos:
                return False

        return True

    except AttributeError:
        return False

    except ValueError:
        return False


def verificar_telefone(telefone):
    """Função que recebe um nome e verifica se o mesmo é válido ou não.
    Caso o nome seja válido retorna True, caso contrário retorna False"""

    caracteres_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ",
                          "+", "(", ")", "-"]

    try:

        valido = False

        for caractere in telefone:

            if str(caractere) in caracteres_validos:
                valido = True

            else:
                valido = False
                break

        return valido

    except AttributeError:
        return False

    except ValueError:
        return False


def verificar_data(dia, mes, ano):
    """
    Função que recebe inteiros referentes ao dia, mês e ano e retorna True
    se a data for válida e False caso seja inválida
    """

    try:

        if mes == 1:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 2:

            # Verificando se o ano informado é um ano bissexto
            if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
                if (dia >= 1) and (dia <= 29):
                    return True

            else:
                if (dia >= 1) and (dia <= 28):
                    return True

        elif mes == 3:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 4:
            if (dia >= 1) and (dia <= 30):
                return True

        elif mes == 5:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 6:
            if (dia >= 1) and (dia <= 30):
                return True

        elif mes == 7:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 8:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 9:
            if (dia >= 1) and (dia <= 30):
                return True

        elif mes == 10:
            if (dia >= 1) and (dia <= 31):
                return True

        elif mes == 11:
            if (dia >= 1) and (dia <= 30):
                return True

        elif mes == 12:
            if (dia >= 1) and (dia <= 31):
                return True

        return False

    except AttributeError:
        return False

    except ValueError:
        return False


if __name__ == "__main__":
    pass
