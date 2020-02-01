

def comer(comida, saudavel):

    if saudavel:
        final = "quero manter a forma."

        return f"Estou comendo {comida} porque {final}"

    else:
        final = "a gente só vive uma vez."

        return f"Estou comendo {comida} porque {final}"


def dormir(num_horas):
    if num_horas > 8:
        return f"Ptz! Dormi muito! Estou atrasado para o trabalho!"

    else:
        return f"Continuo cansado após dormir por {num_horas} horas. :("


def engracado(pessoa):
    comediantes = ["Jim Carrey", "Bozo"]
    if pessoa in comediantes:
        return True
    return False



