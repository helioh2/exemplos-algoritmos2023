


from matrizes import cria_matriz_vazia, print_matriz


def multiplicacao_matrizes(matriz1: list[list], matriz2: list[list]) -> list[list]:

    linhas_m1 = len(matriz1)   # I
    colunas_m1 = len(matriz1[0])  # K

    linhas_m2 = len(matriz2)   # K
    colunas_m2 = len(matriz2[0])   # J

    if colunas_m1 != linhas_m2:
        return "Não é possível multiplicar essas matrizes"


    resultado = cria_matriz_vazia(linhas_m1, colunas_m2, valor_padrao=0)

    # Ver fórmula da mult de matrizes: https://pt.wikipedia.org/wiki/Produto_de_matrizes
    
    for i in range(0, linhas_m1):
        for j in range(0, colunas_m2):

            for k in range(0, colunas_m1):  # ou linhas_m2
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado 




A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 4],
     [2, 5],
     [3, 6]]

print_matriz(multiplicacao_matrizes(A, B))