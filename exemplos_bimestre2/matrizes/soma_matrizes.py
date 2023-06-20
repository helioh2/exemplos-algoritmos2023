


from matrizes import cria_matriz_vazia


def soma_matrizes(m1:list[list], m2:list[list]) -> list[list]:

    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])

    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if linhas_m1 != linhas_m2 or colunas_m1 != colunas_m2:
        print("ERRO: matrizes com dimensões diferentes")
        return None
    
    ## se tiverem dimensões iguais, continua:

    res = cria_matriz_vazia(linhas_m1, colunas_m1)

    for lin in range(0, linhas_m1):
        for col in range(0, colunas_m1):
            res[lin][col] = m1[lin][col] + m2[lin][col]

    return res
    




def soma_matrizes_alt(m1:list[list], m2:list[list]) -> list[list]:

    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])

    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if linhas_m1 == linhas_m2 and colunas_m1 == colunas_m2:
        
        ## se tiverem dimensões iguais, continua:

        res = cria_matriz_vazia(linhas_m1, colunas_m1)

        for lin in range(0, linhas_m1):
            for col in range(0, colunas_m1):
                res[lin][col] = m1[lin][col] + m2[lin][col]

        return res
    
    #"else"
    print("ERRO: matrizes com dimensões diferentes")
    return None

## TESTES

m1 = [[1,2],
      [3,4]]

m2 = [[10,20],
      [30,40]]

resultado_esperado = [
    [11,22],
    [33,44]
]

res = soma_matrizes(m1, m2)
print(res)
assert soma_matrizes(m1, m2) == resultado_esperado