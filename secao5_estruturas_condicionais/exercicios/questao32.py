"""
32) Escrever um programa que leia o código do produto escolhido do cardápio
de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago
por aquele lanche. Considere que a cada execução somente será calculado um
pedido. O cardápio da lanchonete segue o padrão abaixo:

    | Especificação    | Código | Preço |
    | Cachorro Quente  |  100   | 1.20  |
    | Bauru Simples    |  101   | 1.30  |
    | Bauru com Ovo    |  102   | 1.50  |
    | Hamburguer       |  103   | 1.20  |
    | Cheeseburguer    |  104   | 1.70  |
    | Suco             |  105   | 2.20  |
    | Refrigerante     |  106   | 1.00  |

"""

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if codigo == 100:
    preco = 1.20
    print(f"{quantidade} cachorros(s) quente = {preco * quantidade}")

elif codigo == 101:
    preco = 1.30
    print(f"{quantidade} bauru(s) simples = {preco * quantidade}")

elif codigo == 102:
    preco = 1.50
    print(f"{quantidade} bauru(s) com ovo = {preco * quantidade}")

elif codigo == 103:
    preco = 1.20
    print(f"{quantidade} hamburguer(s) = {preco * quantidade}")

elif codigo == 104:
    preco = 1.70
    print(f"{quantidade} cheeseburger(s) = {preco * quantidade}")

elif codigo == 105:
    preco = 2.20
    print(f"{quantidade} suco(s) = {preco * quantidade}")

elif codigo == 106:
    preco = 1.00
    print(f"{quantidade} refrigerante(s) = {preco * quantidade}")

else:
    print("Código inválido!")