"""

class IterandoInfinitamente:

    def __init__(self, iteravel):
        self.tamanho = -1
        self.iteravel = str(iteravel)

    def __iter__(self):
        return self

    def __next__(self):

        if self.tamanho < len(self.iteravel):
            self.tamanho += 1

            if self.tamanho >= 15:
                self.tamanho = 0

            caractere = self.iteravel[self.tamanho]
            return caractere


def iterando_loop(iteravel):
    try:

        it1 = iter(str(iteravel))

        while True:
            print(next(it1))

    except StopIteration:
        pass

    except TypeError:
        print("\nO valor passado por parâmetro deve ser um iterável")


for caractere in IterandoInfinitamente("Geek University"):
    print(caractere)


iterando_loop("Arroz e Carne")
iterando_loop(True)
iterando_loop(12321342)


from time import time

tempo_inicial = time()
print(sum((i for i in range(120093020))))
gen_tempo = time() - tempo_inicial

tempo_inicial = time()
print(sum([i for i in range(120093020) if i % 2 == 0]))
list_tempo = time() - tempo_inicial

print(f"Usando generator expression: {gen_tempo} s")
print(f"Usando list expression: {list_tempo} s")

"""


def fatoriais_generator(maximo):
    for n in range(1, maximo):
        fatorial = 1

        for f in range(1, n):
            fatorial *= f

        yield fatorial


def fatoriais_lista(maximo):

    fatoriais = []

    for n in range(1, maximo):
        fatorial = 1

        for f in range(1, n):
            fatorial *= f

        fatoriais.append(fatorial)

    return fatoriais


generator = list(fatoriais_generator(100))
lista = fatoriais_lista(100)

print(generator)
print(lista)
