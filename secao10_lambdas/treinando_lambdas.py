#
# calc = lambda x: x ** 2
#
# num = int(input("Numero: "))
# print(calc(num))
#
# nomes = ["Pedro Henrique Gomes Lima", "Aquila Rodrigues Menezes", "Guidon de Bicicleta",
#          "Alexia Gorda", "Rian Marlon S. da Silva"]
#
# nomes.sort(key=lambda sobrenome: sobrenome.split()[-1].lower())
#
# print(nomes)
#
#
# cronometro = lambda x: [print(i) for i in range(x, -1, -1) if i % 2 == 0]
#
# cronometro(100)
#
# nomes = ["João Guilherme", "Rian Marlon", "Guidon de Bicicleta", "Pedro Henrique",
#          "Dalker Pinheiro", "Carlos Vinicius", "Aquila Menezes", "Vitor Emanuel", "Francisco Nogueira",
#          "Lucas Ravel", "Lara Alessandra", "Ana Beatri,", "Felipe Lima", "Felipe dos Anjos", "Ermerson Aguiar",
#          "Victor Ravel", "Raimundo Argermiro", "Raimundo Neto", "Gabriel Viana"]
#
# nomes.sort(key=lambda segundo_nome: segundo_nome.split()[-1].lower())
# print(nomes)
#
#
# def equacao_simples(y, z):
#     """Realiza o cálculo de uma função simples"""
#     return lambda x: (y ** 2 + z * 5 / z) ** x
#
#
# print(equacao_simples(12, 43)(4))

# Map

# numeros = [23, 56, 576, 65, 434, 23, 89, 34]
#
# calculo = list(map(lambda numero: (numero * 2) ** 2, numeros))
# print(calculo)
#
# professores = ["Vanessa", "Ana", "Lara", "Cintia", "Julia"]
#
# # Usando filter e map
# [print(i) for i in list(map(lambda professora: f"O nome da sua professora é {professora}",
#                         filter(lambda nome: len(nome) > 5, professores)))]
#
# usuarios = [
#     {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
#     {"username": "carla", "tweets": ["Eu amo meu gato"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": []},
#     {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
#     {"username": "gal", "tweets": []}
# ]
#
# print(usuarios)
#
# # Filtrar os usuários que estão inativos no Twitter
#
# [print(i) for i in list(filter(lambda usuario: not len(usuario["tweets"]) > 0, usuarios))]
#
# from statistics import mean
#
# numeros = [24, 732, 845, 4863, 434, 4034, 54, 3255]
# print(mean(numeros))
#
# acima_da_media = list(filter(lambda numero: numero > mean(numeros), numeros))
# print(acima_da_media)
#
# nomes = ["Pedro Henrique Gomes Lima", "Lucas Ravel Pinto", "Vitor Emanuel", "Franciscso Nogueira",
#          "Francisco Gleison", "Lara Alessandra", "Welligton Almeida"]
#
# apenas2 = list(filter(lambda nome: not len(nome.split()) > 2, nomes))
# print(apenas2)
#
#
# musicas = [{"musica": "Lady Gaga", "autor": "Mc Igu"},
#            {"musica": "Frozen", "autor": "Mc Igu"},
#            {"musica": "Rap da Roça", "autor": ""},
#            {"musica": "Zé Gaguinho", "autor": ""},
#            {"musica": "Olho por Olho", "autor": "Lil Raff"},
#            {"musica": "Bank Account", "autor": "21 Savage"},
#            {"musica": "Evoluiu", "autor": ""},
#            {"musica": "Uzi", "autor": "Mc Igu"},
#            {"musica": "Tic Tac", "autor": "Aka Rasta"},
#            {"musica": "10K", "autor": "Lil Raff"},
#            {"musica": "Burn Down", "autor": ""},
#            {"musica": "Michael Myers", "autor": "Mc Igu"},
#            {"musica": "Made in Chernobyl3", "autor": "Letodie"},
#            {"musica": "Gallantry", "autor": ""}]
#
# [print(autor_musica) for autor_musica in list(map(lambda musica: f"{musica['autor']} - {musica['musica']}",
#                                               filter(lambda musica: musica["autor"], musicas)))]
#
# from statistics import mean
#
# pessoas = [["Rian Marlon", 17, 73], ["Welligton Almeida", 16, 60], ["Lara Emylle", 15, 52],
#            ["Francisco Nogueira", 16, 70], ["Pedro Henrique", 16, 63], ["Lucas Ravel", 16, 68],
#            ["Vitor Emanuel", 16, 62], ["Carlos Vinicius", 16, 65.9]]
#
# media_peso = mean(list(map(lambda pessoa: pessoa[2], pessoas)))
#
# print(f"A média do peso: {media_peso}")
#
# Reduce
#
# from functools import reduce
#
# numeros = [32, 65, 87, 98, 87, 879]
#
# print(reduce(lambda num1, num2: num1 + num2, numeros))
#
#
# numeros = [786, 67, 87, 3]
#
# print(reduce(lambda num1, num2: num1 / num2, numeros))
#
#
# numeros = [87, 988, 96, 57, 83, 34, 12, 21, 37]
#
# print(reduce(lambda num1, num2: num1 + (num1 * num2), numeros))
#
#
# numeros = [3, 43, 2, 5, 43, 7]
#
# print(reduce(lambda num1, num2: num1 + num2 + (num1 * num1) / (num2**num2), numeros))

# Any e ALL

# numeros = [43, 34, 332, 32, 0, -34]
#
# print(all([num for num in numeros]))
#
# print(any([num for num in numeros]))

# nomes = ["Carlos Vinicius", "Eduardo Bezerra", "Carla Saraiva", "Chico Borges"]
#
# print(all([nome[0].lower() == 'c' for nome in nomes]))
# print(any([nome[0].lower() == 'c' for nome in nomes]))

# Generators

# from sys import getsizeof

# generator = (i for i in range(1, 1000) if i % 2 == 0)
# print(getsizeof(generator))
#
# list_comprehension = [i for i in range(1, 1000) if i % 2 == 0]
# print(getsizeof(list_comprehension))
#
# nomes = ["Carlos Vinicius", "Eduardo Bezerra", "Carla Saraiva", "Chico Borges", "Francisco Filho",
#          "Gleison Martins", "Barbara Almeida", "Rian Marlon"]

# Usando Generator Expression
# print(any(nome[0].upper() == "C" for nome in nomes))
# print(all(nome[0].upper() == "C" for nome in nomes))
#
# Quantidade de Bytes usado
# print(getsizeof(any(nome[0].upper() == "C" for nome in nomes)))
# print(getsizeof(all(nome[0].upper() == "C" for nome in nomes)))

# [print(nome) for nome in nomes if len(nome.split()[0]) >= 6]
#
# generator2 = (nome for nome in nomes if len(nome.split()[0]) >= 6)
# print(getsizeof(generator2))
#
# list_comprehension2 = [nome for nome in nomes if len(nome.split()[0]) >= 6]
# print(getsizeof(list_comprehension2))

# print(sorted(nomes, key=lambda nome: nome.split()[-1]))
#
# musicas = [
#     {"titulo": "Sensacional", "tocou": 200},
#     {"titulo": "10K", "tocou": 100},
#     {"titulo": "Uzi", "tocou": 300},
#     {"titulo": "Lady Gaga", "tocou": 50},
#     {"titulo": "Frozen", "tocou": 80},
#     {"titulo": "Plaqtudum", "tocou": 240},
#     {"titulo": "Buenos Aires", "tocou": 20},
#     {"titulo": "Tic Tac", "tocou": 230},
#     {"titulo": "Olho por Olho", "tocou": 20}
# ]
#
# Organizando pelas mais tocadas
# print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
# print(sorted(musicas, key=lambda musica: musica["tocou"]))
#
# Organizando por titulo
# print(sorted(musicas, key=lambda musica: musica["titulo"], reverse=False))
# print(sorted(musicas, key=lambda musica: musica["titulo"]))
#
# usuarios = [
#     {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
#     {"username": "carla", "tweets": ["Eu amo meu gato"]},
#     {"username": "jeff", "tweets": []},
#     {"username": "bob123", "tweets": [], "cor": "amarelo"},
#     {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
#     {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
# ]
#
# Organizando os usuário por nome
# print(sorted(usuarios, key=lambda usuario: usuario["username"]))
# print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
#
# Organizando pela quantidade de tweets
# print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
# print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))
#
# min e max
#
# musicas = [
#     {"titulo": "Sensacional", "tocou": 200},
#     {"titulo": "10K", "tocou": 100},
#     {"titulo": "Uzi", "tocou": 300},
#     {"titulo": "Lady Gaga", "tocou": 50},
#     {"titulo": "Frozen", "tocou": 80},
#     {"titulo": "Plaqtudum", "tocou": 240},
#     {"titulo": "Buenos Aires", "tocou": 20},
#     {"titulo": "Tic Tac", "tocou": 230},
#     {"titulo": "Olho por Olho", "tocou": 20}
# ]
#
# A quantidade de vezes que a música mais tocada, tocou
# print(max(musicas, key=lambda musica: musica["tocou"]))
#
# A quantidade de vezes que a música menos tocada, tocou
# print(min(musicas, key=lambda musica: musica["tocou"]))
#
# O título da música mais tocada
# print((max(musicas, key=lambda musica: musica["tocou"])["titulo"]))
#
# O título da música menos tocada
# print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])
#
# nomes = ["Carlos Vinicius", "Eduardo Bezerra", "Carla Saraiva", "Chico Borges", "Francisco Filho Joaquim",
#          "Gleison Martins", "Barbara Almeida", "Rian Marlon"]
#
# # O maior nome
# print(max(nomes, key=lambda nome: len(nome)))
#
# # O menor nome
# print(max(nomes, key=lambda nome: len(nome)))
#
#
# frase = "O rabo da lagartixa é amarelo"
#
# print("".join(reversed(frase)))
# print(frase[::-1])

# [print(palavra) for palavra in "Batatinha quando nasce se esparrama pelo chão".split() if 'e' in palavra]

# ABS
#
# print(abs(-34))
# print(abs(-76))
# print(abs(132))
# print(abs(-132))

# absoluto1 = abs(-3534)
# absoluto2 = abs(-234.76867)
# absoluto3 = abs(3442)
# absoluto4 = abs(-6589.54664)
# absoluto5 = abs(990)
#
# print(*[absoluto1, absoluto2, absoluto3, absoluto4, absoluto5])
#
# [print(absoluto) for absoluto in [absoluto1, absoluto2, absoluto3, absoluto4, absoluto5]]

# ROUND

# print(round(43.984332, 2))
# print(round(45.51))
# print(round(76.766998944, 3))
# print(round(4.501))
# print(round(76.49999))

# ZIP

# Média final de cada aluno

# from statistics import mean
#
# notas1 = [5.6, 7.6, 6.5, 4.5, 6.5, 5.6, 7.6, 9.0, 4.5]
# notas2 = [7.6, 9.6, 8.3, 7.2, 9.4, 6.6, 8.5, 7.9, 10.0]
# notas3 = [5.9, 8.6, 5.5, 6.7, 8.8, 9.2, 9.3, 4.7, 5.7]
# notas4 = [4.2, 7.0, 6.7, 4.0, 8.0, 6.9, 9.0, 5.5, 5.5]
#
# alunos = ["Pedro Henrique", "Aquila Menezes", "Vitor Emanuel", "Lucas Ravel",
#           "Raimundo Neto", "Rian Marlon", "Carlos Vinicius", "Pierre Neves",
#           "Welligton Almeida"]

# Faz a média usando a função mean(), e depois atráves da função round(), arredonda para 1 casa decimal
# a média de cada aluno

# 1° Forma
# media_final = {aluno[0]: round(mean([aluno[1], aluno[2], aluno[3], aluno[4]]), 1)
#                for aluno in zip(alunos, notas1, notas2, notas3, notas4)}

# print(media_final)

# 2° Forma
# media_final2 = zip(alunos, map(lambda nota: round(mean(nota), 1), zip(notas1, notas2, notas3, notas4)))
#
# print(dict(media_final2))

# [print(f"Aluno: {aluno} - Média final: {media}") for aluno, media in media_final.items()]
#
# print()

# O aluno com a menor média

# 1° Forma

# media.keys() irá pegar o nome de cada aluno
# media_final[aluno] irá verificar a média final do aluno
# print(min(media_final.keys(), key=lambda aluno: media_final[aluno]))

# 2° Forma

# Pega a menor média
# menor = min(media_final.values())
# Filtra o(s) aluno(s) que possue(m) a menor média
# print(*list(filter(lambda nome: media_final[nome] == menor, media_final.keys())))

# O aluno com a maior média

# 1° Forma
# print(max(media_final.keys(), key=lambda aluno: media_final[aluno]))

# 2°Forma

# maior = max(media_final.values())
# print(*list(filter(lambda nome: media_final[nome] == maior, media_final.keys())))

velocidade_maxima = [200, 345, 189, 230, 150, 300, 220, 280]
carros = ["Audi A3 Cabriolet", "McLaren - MCL34", "HB20", "Lamborghini Gallardo Squadra Corse",
          "Gol", "Racing Point - RP19", "Porsche 918 Spyder", "Toro Rosso - STR14", "wewewewe"]

quantidade_ids = range(1, len(velocidade_maxima)+1) if len(velocidade_maxima) < len(carros) \
                 else range(1, len(carros)+1)

carros_velocidade = dict(zip(quantidade_ids, zip(carros, velocidade_maxima)))

print(carros_velocidade)

print(f"\nO CARRO MAIS RÁPIDO DA LISTA DE CARROS: ")

# Identificador do carro mais rápido
rapido = max(carros_velocidade.keys(), key=lambda identificador: carros_velocidade[identificador][1])

# Imprimir o nome do carro
print(carros_velocidade[rapido][0])

print(f"\nO CARRO MAIS LENTO DA LISTA DE CARROS: ")

# Identificador do carro mais lento
lento = min(carros_velocidade.keys(), key=lambda identificador: carros_velocidade[identificador][1])
print(carros_velocidade[lento][0])
