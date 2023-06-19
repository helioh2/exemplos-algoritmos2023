




from matrizes import cria_matriz_vazia


def multiplica_por_dois(matriz: list[list]):
    """Versão modificadora"""
    if len(matriz) == 0:
        return  #termina

    linhas = len(matriz)
    colunas = len(matriz[0])

    for lin in range(0, linhas):
        for col in range(0, colunas):
            matriz[lin][col] = matriz[lin][col] * 2



def multiplica_por_dois_pura(matriz: list[list]):

    if len(matriz) == 0:
        return matriz

    linhas = len(matriz)
    colunas = len(matriz[0])

    res = cria_matriz_vazia(linhas, colunas)

    print(res) #debug (descobrir o que está acontecendo) apagar depois
    print(matriz)

    for lin in range(0, linhas):
        for col in range(0, colunas):
            res[lin][col] = matriz[lin][col]*2

    return res




## TESTES:

m1 = [[1,2],
      [3,4]]

# multiplica_por_dois(m1)

# print(m1)


m2 = multiplica_por_dois_pura(m1)

print(m1)
print(m2)