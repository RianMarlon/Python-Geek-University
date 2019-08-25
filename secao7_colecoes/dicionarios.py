"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))


# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusice lista, tupla dicionário, como chaves
# de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas
# são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado)  # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Paystation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.


# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))


usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
