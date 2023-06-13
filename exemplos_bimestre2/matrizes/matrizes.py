

def cria_matriz_vazia_v0(linhas, colunas):
    matriz = [None]*linhas
    for lin in range(linhas):
        matriz[lin] = [None]*colunas
    return matriz


def cria_matriz_vazia(linhas, colunas, valor_padrao=None):
    return [[valor_padrao]*colunas for _ in range(linhas)]


def print_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for lin in range(0, linhas):
        for col in range(0, colunas):
            print(str(matriz[lin][col])+",\t", end="")
        print()





## PROGRAMA PRINCIPAL

matriz = cria_matriz_vazia(4, 5)

print(matriz)

matriz[1][1] = 10

print_matriz(matriz)


