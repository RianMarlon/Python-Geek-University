"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissao de Leitura -> Para ler o arquivo
    - Permissão de Escrita -> Para escrever no arquivo

StringIO -> Utilizado paral er e criar arquivos em memória

"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Uma mensagem\n'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# arquivo = open('arq.txt', 'w')

# Agora, tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Inserindo mais um texto
arquivo.write('Uma nova mensagem')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())



