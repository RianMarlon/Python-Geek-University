"""
71) Considerando a estrutura:

    struct Ponto{
    int x;
    int y;
    };

Para representar um ponto em uma grade 2D, implemente uma função que indique se um
ponto p está localicado dentro ou fora de um retângulo. O retângulo é definico
por seus vértices inferior esquerdo v1 e superior direito v2. A função deve retornar
1 caso o ponto esteja localizado dentro do retângulo e 0 caso contrário. Essa função deve
obedecer ao protótipo:

int dentroRet (struct Ponto* v1, struct Ponto* v2, struct Ponto* p);
"""


def dentro_ret(x1, y1, x2, y2, p1, p2):
    """
    Função que recebe as posições do vértice inferior esquerdo e superior direto de um
    retângulo
    :param x1: Recebe a posição da coordenada X do vértice inferior esquerdo do retângulo
    :param y1: Recebe a posição da coordenada Y do vértice inferior esquerdo do retângulo
    :param x2: Recebe a posição da coordenada X do vértice superior direito do retângulo
    :param y2: Recebe a posição da coordenada Y do vértice superior direito do retângulo
    :param p1: Recebe a posição da coordenada X do ponto indicado
    :param p2: Recebe a posição da coordenada Y do ponto indicado
    :return: Retorna 1 caso as coodernadas informadas esteja dentro do retângulo e 0 caso
    contrário. Caso os valores informados sejam inválidos, retorna TypeError
    """

    if (x1 <= p1) and (x2 >= p1):
        if (y1 <= p2) and (y2 >= p2):
            return 1

    return 0


coordenada_x1 = int(input("Local da coordenada x do vértice inferior esquerdo do retângulo: "))
coordenada_y1 = int(input("Local da coordenada y do vértice inferior esquerdo do retângulo: "))
coordenada_x2 = int(input("\nLocal da coordenada x do vértice superior direita do retângulo: "))
coordenada_y2 = int(input("Local da coordenada y do vértice superior direita do retângulo: "))

coordenada_p1 = int(input("\nLocal da coordenada x do ponto: "))
coordenada_p2 = int(input("Local da coordenada y do ponto: "))

print(f"\n{dentro_ret(coordenada_x1, coordenada_y1, coordenada_x2, coordenada_y2, coordenada_p1, coordenada_p2)}")
