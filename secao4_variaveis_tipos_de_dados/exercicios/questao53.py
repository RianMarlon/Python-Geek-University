"""
53) Faça umm programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela.
"""

c = float(input("Digite o tamanho da comprimento em metros: "))
l = float(input("Digite o tamanho da largura em metros: "))

p = float(input("\nDigite o preço do metro de tela: "))

preco = (c * 2 + l * 2) * p

print("\nO curso para cercar o terreno com tela:\n"
      "%.2f" % preco)

