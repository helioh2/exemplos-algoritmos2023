


from matrizes import cria_matriz_vazia


def rotacionar(matriz):
    
    linhas = len(matriz)
    colunas = len(matriz[0])

    res = cria_matriz_vazia(linhas, colunas)

    for lin in range(0, linhas):
        for col in range(0, colunas):
            ## matriz[0][0] --> res[2][0]
            ## matriz[0][1] --> res[1][0]
            ## matriz[0][2] --> res[0][0]

            ## matriz[1][0] --> res[2][1]
            ## matriz[1][1] --> res[1][1]
            ## matriz[1][2] --> res[0][1]

            ## matriz[2][0] --> res[2][2]
            ## matriz[2][1] --> res[1][2]
            ## matriz[2][2] --> res[0][2]

            ## LOGO: matriz[lin][col] --> res[colunas-col-1][lin]
            res[colunas-col-1][lin] = matriz[lin][col]

    return res


##TESTES:

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]


m2 = rotacionar(m1)
esperado = [[3,6,9],
            [2,5,8],
            [1,4,7]]

print(rotacionar(m1))
assert rotacionar(m1) == esperado