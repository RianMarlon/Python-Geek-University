"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arq.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Paths relativos
print(os.path.exists('geek4'))  # True
print(os.path.exists('geek4/university'))  # True
print(os.path.exists('geek4/university/geek3.py'))  # False
print(os.path.exists('outro'))  # False

# Paths absolutos
print(os.path.exists('C:\\developer\\Python\\geek'))  # False
print(os.path.exists('C:\\Users\\RianM\\OneDrive\\Imagens'))  # True
print(os.path.exists('C:\\Users\\RianM\\OneDrive\\Imagens\\natureza.png'))  # True

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Renomear arquivos e diretórios

# Diretórios
os.rename('geek2', 'geek')

# OBS: Se o diretório não existir, teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear, não estiver vazio, teremos um OSError

# Arquivos
os.rename('arquivo-teste2.txt', 'arquivo-teste3.txt')
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório,
# eles não vão para a lixeira. Eles somem.

# Removendo arquivos
os.remove('geek')

# OBS: Se você estiver no Windows e o arquivo que vocÊ for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError ou um
# PermissionError (no Windows)

# Removendo diretórios vazios
os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir, teremos um FileNotFoundError

# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek'):

    print(f" - {arquivo.name}")
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretório vazios
os.removedirs('geek2/arquivos')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as temp:
    print(f"Criei o diretório temporário em {temp}")

    with open(os.path.join(temp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo escrevendo um texto. No final, usamos um input() só apra mantermos
# os arquivos temporários 'vivos' dentro dos blocos with

# Criando um arquivo temporário

with tempfile.TemporaryFile() as temp:
    temp.write(b'Geek Univerisity\n')
    temp.seek(0)
    print(temp.read())

# OBS: Em arquivos temporário só conseguimos escrever bits. Por isso, utilizamos b

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b"Geek University\n")
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b"geek University\n")

print(arquivo.name)
print(arquivo.read())

input()
arquivo.close()

https://docs.python.org/3/library/os.html

"""
