#
#
# def soma(num1, num2):
#     """Realiza a soma de dois números"""
#
#     if (type(num1) is not int) and (type(num1) is not float):
#         raise TypeError("A função recebe apenas valores numéricos!")
#
#     if (type(num2) is not int) and (type(num2) is not float):
#         raise TypeError("A função recebe apenas valores numéricos!")
#
#     print(f"{num1} + {num2} = {num1 + num2}")
#
#
# soma(978.9, '98')
#
#
#

# try:
#     len('5')
#     print(geek)
#
# except TypeError:
#     print("Não pode passar um número como parâmetro na função len()")
#
# except NameError:
#     print("A váriavel não foi criada")


# def dividir(num1, num2):
#     try:
#         print(f"{int(num1)} / {int(num2)} = {int(num1) / int(num2)}")
#
#     except ValueError:
#         print("A função deve receber apenas valores que podem ser convertidos em números")
#
#     except ZeroDivisionError:
#         print("Não pode dividir um número por zero")
#
#     else:
#         print("FIM DA FUNÇÃO")
#
#
# dividir('8', '0')


# def colore_texto(texto, cor):
#
#     try:
#         cor = cor.strip().lower()
#         cores = {"vermelho": "\033[31m", "verde": "\033[32m", "amarelo": "\033[33m",
#                  "azul": "\033[34m", "roxo": "\033[35m", "ciano": "\033[36m", "cinza": "\033[37m"}
#
#         if cor in cores.keys():
#             print(f"{cores[cor]}{texto}")
#
#         else:
#             raise ValueError
#
#     except AttributeError:
#         print(f"A função deve receber apenas valores do tipo string")
#
#     except ValueError:
#         print("Cor inválida")
#
#
# texto1 = str(input("Digite um texto/frase: "))
# cor1 = str(input("Qual a cor que você deseja colocar no texto? "))
#
# print()
#
# colore_texto(texto1, cor1)

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    calc = num1 / num2 + num1 ** num2

    print(f"\n{calc}")

except ValueError as ve:
    print(f"\nApenas valores numéricos... {ve}")

except ZeroDivisionError as zd:
    print(f"\nNão pode dividir um número por zero... {zd}")

finally:
    print("\nFIM DO PROGRAMA")
