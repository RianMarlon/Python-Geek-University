"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)


for letra in 'Geek University':
    print(letra)


iter([1, 2, 3, 4, 5])

iter('Geek University')
"""


def meu_for(interavel):

    try:
        it = iter(interavel)
        while True:
            print(next(it))

    except StopIteration:
        pass

    except TypeError:
        print("\nO valor passado por parâmetro tem que ser um iterável!")


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)

meu_for(True)

meu_for(344)

