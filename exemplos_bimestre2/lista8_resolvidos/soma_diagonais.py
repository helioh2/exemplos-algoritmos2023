


def soma_todos(matriz: list[list]): 

    linhas = len(matriz)
    colunas = len(matriz[0])

    soma = 0

    for lin in range(0, linhas):
        for col in range(0, colunas):
            soma += matriz[lin][col]

    return soma


def soma_diagonal_principal(matriz: list[list]): 

    linhas = len(matriz)
    colunas = len(matriz[0])

    soma = 0

    for lin in range(0, linhas):
        for col in range(0, colunas):
            if lin == col:
                soma += matriz[lin][col]

    return soma



def soma_diagonal_secundaria(matriz: list[list]): 

    linhas = len(matriz)
    colunas = len(matriz[0])

    soma = 0

    for lin in range(0, linhas):
        for col in range(0, colunas):
            if abs(lin) == abs(col-(colunas-1)):  # ou: lin == colunas-col-1
                soma += matriz[lin][col]

    return soma


def soma_diagonais(matriz: list[list]):
    """
    Versão mais espertinha
    """

    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        print("ERRO: matriz não quadrada")
        return

    soma = 0
    n = linhas

    for i in range(0, n):
        soma += matriz[i][i]  # diagonal principal
        soma += matriz[i][n-i-1]   # diagonal secundária

    return soma



## TESTES/EXEMPLOS

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]  # 3x3

m2 = [[1,2,3,10],
      [4,5,6,20],
      [7,8,9,30],
      [10,11,20,40]]  # 4x4

## diagonal principal: soma o (0,0), (1,1) e (2,2) 
## diagonal secundario: soma o (0,2), (1,1) e (2,0)  --> 2 = 3-1 = n-1  (lin, col-(colunas-1))

##  (0,2) --> (lin, col-(colunas-1))
## (2,0)  --> (lin-(linhas-1),col)
## (1,1)   -->  (abs(1), abs(-1))


## (0,3) --> (lin, col-(colunas-1))
## (1,2) --> (lin, col-(colunas-1)) --> (1, abs(-1))
## (1,2) --> (lin-(linhas-1),col) --> (abs(-2),2)

# print(soma_todos(m1))
assert soma_todos(m1) == 45


# print(soma_diagonal_secundaria(m2))


print(soma_diagonais(m1))
print(soma_diagonais(m2))