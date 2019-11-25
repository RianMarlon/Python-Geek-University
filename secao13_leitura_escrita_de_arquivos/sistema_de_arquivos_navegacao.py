"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Sistema Operacional

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
# print(os.path.isabs(os.getcwd()))

print(os.getcwd())  # C:\\developer\\Python\\geek university\\aulas\\secao13_leitura_escrita_de_arquivos

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())  # C:\\developer\\Python\\geek university\\aulas

os.chdir('..')
print(os.getcwd())  # C:\\developer\\Python\\geek university

os.chdir('..')
print(os.getcwd())  # C:\\developer\\Python

os.chdir('..')
print(os.getcwd())  # C:\\developer

os.chdir('..')
print(os.getcwd())  # C:\

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('C:\\developer\\Python\\geek university'))  # True

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes do sistema operacional
# print(os.uname())  # Funciona no Linux e Mac (Windows não funciona)

# Fazer o import
from os import sys

print(sys.platform)  # Funciona em todos os sistemas operacionais

# C:\\developer\\Python\\geek university\\aulas\\secao13_leitura_escrita_de_arquivos
print(os.getcwd())

local = os.path.join(os.getcwd(), 'geek4', 'university')

os.chdir(local)

# C:\\developer\\Python\\geek university\\aulas\\secao13_leitura_escrita_de_arquivos\\geek4\\university
print(os.getcwd())

# Veja que o os.path.join() recebe dpis parâmetros, sendo o primeiro o diretório atual e o segundo
# o diretório que será juntado ao atual

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir(os.getcwd()))
print(len(os.listdir(os.getcwd())))

print(os.listdir('C:\\'))
print(len(os.listdir('C:\\')))


"""

# Fazer o import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

scanner = os.scandir()

arquivos = list(scanner)

# [print(arquivo.name) for arquivo in arquivos]  # nome do arquivo

print(dir(arquivos[0]))

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas...

# OBS: quando usamos o scandir() nós precisamos fechá-la, assim como abrimos um arquivo

scanner.close()
