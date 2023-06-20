


from matrizes import cria_matriz_vazia, print_matriz


def multiplicacao_matrizes(m1: list[list], m2: list[list]) -> list[list]:

    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])

    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if colunas_m1 != linhas_m2:  # não dá certo
        print("ERRO: matrizes incompatíveis para multiplicação")
        return None
    
    #"else"

    res = cria_matriz_vazia(linhas_m1, colunas_m2)

    for lin in range(0, linhas_m1):
        for col in range(0, colunas_m2):
            res[lin][col] = 0  #inicializa posição na resultante com 0, pra fazer a soma
            for k in range(0, colunas_m1): #ou linhas_m2
                res[lin][col] += m1[lin][k] * m2[k][col]

    return res



   




A = [[1, 2, 3],
     [4, 5, 6]]   #2x3

B = [[10, 40],
     [20, 50],
     [30, 60]]   #3x2


C = [[140, 320],
     [320, 770]]   #2x2

print_matriz(multiplicacao_matrizes(A, B))
assert multiplicacao_matrizes(A,B) == C