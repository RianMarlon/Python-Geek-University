"""
73) Foi realizada uma pesquisa de algumas características físicas de cinco
habitantes de certa região. De cada habitante foram coletados os seguintes
dados: sexo, cor dos olhos (A - Azuis ou C - Castanhos), cor dos cabelos
(L - Louros, P - Pretos ou C - Castanhos) e idade

    . Faça uma função que leia esses dados em um vetor
    . Faça uma função que determine a média de idade das pessoas
    com olhos castanhos e cabelos pretos
    . Faça uma função que determine e devolva ao programa principal a maior
    idade entre os habitantes
    . Faça uma função que determine e devolva ao programa principal a quantidade
    de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que
    tenham olhos azuis e cabelos louros
"""


def ler_dados():
    """
    Função que ler os dados de um habitante de certa região e armazena em um vetor
    :return: Retorna o vetor preenchido com as informações fornecidas
    """

    habitantes = []

    for i in range(5):
        informacoes = []

        sexo = ''
        while not(sexo == "masculino" or sexo == "feminino"):
            sexo = str(input(f"Sexo do habitante {i+1} (masculino / feminino): "))
            sexo = sexo.lower()
        informacoes.append(sexo)

        cor_olhos = ''
        while not(cor_olhos == "azuis" or cor_olhos == "castanhos"):
            cor_olhos = str(input(f"Cor dos olhos do habitante {i+1} (azuis / castanhos): "))
            cor_olhos = cor_olhos.lower()
        informacoes.append(cor_olhos.lower())

        cor_cabelos = ''
        while not(cor_cabelos == "louro" or cor_cabelos == "preto" or cor_cabelos == "castanho"):
            cor_cabelos = str(input(f"Cor do cabelo do habitante {i+1} (Louro / Preto / Castanho): "))
            cor_cabelos = cor_cabelos.lower()
        informacoes.append(cor_cabelos)

        idade = int(input(f"Idade do habitante {i+1}: "))
        informacoes.append(idade)

        print()

        habitantes.append(informacoes)

    return habitantes


def media(args):
    """
    Função que recebe uma matriz com as informações de cada habitante e imprimi no console
    a média de idade das pessoas com olhos castanhos e cabelos pretos. Caso não possua a quantidade
    de dados necessário, imprimi no console que os dados são inválidos.
    :param args: Recebe uma matriz com as informações de cada habitante que recebeu os dados
    através da função ler_dados()
    """

    dados1 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados1 = False

    else:
        dados1 = False

    if dados1:
        soma_idade = 0
        qtd = 0

        for i in range(5):

            if args[i][1] == 'castanhos':
                if args[i][2] == 'preto':
                    soma_idade += args[i][3]
                    qtd += 1

        print(f"Média de idade das pessoas com olhos castanhos e cabelos pretos: {int(soma_idade / qtd)}")

    else:
        print("Dados inválidos")


def maior_idade(args):
    """
    Função que recebe uma matriz com as informações dos habitantes e retorna a maior
    idade entre os habitantes
    :param args: Recebe uma matriz com as informações de cada habitante que recebeu os dados
    através da função ler_dados()
    :return: retorna a maior idade entre os habitantes. Caso a matriz não possua um tamanho válido
    retorna um valor do tipo None
    """

    dados2 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados2 = False

    else:
        dados2 = False

    if dados2:
        maior = []

        for i in range(5):
            maior.append(args[i][3])

        return max(maior)


def qtd_individuos(args):
    """
    Função que recebe uma matriz com as informações de cada habitante e retorna a quantidade
    de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que
    tenham olhos azuis e cabelos louros
    :param args: Recebe uma matriz com as informações de cada habitante que recebeu os dados
    através da função ler_dados()
    :return: Retorna a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35
    (inclusive) e que tenham olhos azuis e cabelos louros. Caso a matriz não possua um tamanho válido
    retorna um valor do tipo None
    """

    dados3 = True

    if len(args) == 5:
        for i in range(len(args)):
            if len(args[i]) != 4:
                dados3 = False

    else:
        dados3 = False

    if dados3:
        quantidade = 0

        for i in range(5):

            if args[i][0] == 'feminino' and args[i][1] == 'azuis':
                if (args[i][2] == 'louro') and (args[i][3] >= 18) and (args[i][3] <= 35):
                    quantidade += 1

        return quantidade


dados = ler_dados()
media(dados)
print(f"A maior idade entre os habitantes: {maior_idade(dados)}")
print(f"Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) "
      f"e que tenham olhos azuis e cabelos louros: {qtd_individuos(dados)}")
