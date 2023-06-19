


from matrizes import cria_matriz_vazia


def transposta(matriz: list[list]) -> list[list]:
    
    linhas = len(matriz)
    colunas = len(matriz[0])

    res = cria_matriz_vazia(colunas, linhas)  #2x3  --> 3x2

    for lin in range(0, linhas):
        for col in range(0, colunas):
            res[col][lin] = matriz[lin][col]

    # também funciona assim:
    # for lin in range(0, colunas):
    #     for col in range(0, linhas):
    #         res[lin][col] = matriz[col][lin]

    return res


def transposta_modificadora(matriz: list[list]):
    """
    Só funciona com matrizes quadradas (linhas=colunas)
    """
     
    linhas = len(matriz)
    colunas = len(matriz[0])

    for lin in range(0, linhas-1):
        for col in range(lin+1, colunas):
            ## Realiza a troca dos valores de matriz[lin][col] por matriz[col][lin] e vice-versa
            temp = matriz[col][lin]
            matriz[col][lin] = matriz[lin][col]
            matriz[lin][col] = temp

    # também funciona assim:
    # for lin in range(1, linhas):
    #     for col in range(0, lin):
    #         temp = matriz[col][lin]
    #         matriz[col][lin] = matriz[lin][col]
    #         matriz[lin][col] = temp
    





##TESTES:

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]


m2 = transposta(m1)

print(m2)

# print(m1)

"""
[[1, 4, 7], 
[2, 5, 8], 
[3, 6, 9]]
"""

m3 = [[1,2,3],
      [4,5,6]]

m4 = transposta(m3)
print(m4)

"""
[[1, 4], 
[2, 5], 
[3, 6]]
"""


transposta_modificadora(m1)

print(m1)

"""
[[1, 4, 7], 
[2, 5, 8], 
[3, 6, 9]]
"""