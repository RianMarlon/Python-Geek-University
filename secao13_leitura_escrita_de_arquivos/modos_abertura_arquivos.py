"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão.
w -> Abre para escrita - sobrescreve caso o arquivo já existar.
x -> Abre para escrita somente se o arquivo não existir. Caso exista, gera FileExistError.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: leitura e escrita (temos controle do cursor, usando r e o w)

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adiconado SEMPRE ao final do arquivo. Com o modo 'a' não controlamos o cursor.

https://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo a
with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = str(input("Informe uma fruta ou sair: "))

        if fruta.strip().lower() != 'sair':
            arquivo.write(fruta+'\n')

        else:
            break

# Exemplo r+
with open('outro.txt', 'r+', encoding='utf-8') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')

"""
