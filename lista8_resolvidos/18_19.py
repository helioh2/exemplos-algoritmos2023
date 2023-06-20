

def cria_matriz_vazia(linhas, colunas, valor_padrao=None):
    return [[valor_padrao]*colunas for _ in range(linhas)]



def print_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for lin in range(0, linhas):
        for col in range(0, colunas):
            print(str(matriz[lin][col])+",\t", end="")
        print()


linhas = 4
colunas = 10
m1 = cria_matriz_vazia(linhas, colunas)

contador = 0

for lin in range(0, linhas):
    for col in range(0, colunas):
        m1[lin][col] = contador
        contador += 1

print_matriz(m1)

linhas = 10
colunas = 4
m2 = cria_matriz_vazia(linhas, colunas)

contador = 0

for col in range(0, colunas):
    for lin in range(0, linhas):
        m2[lin][col] = contador
        contador += 1

print_matriz(m2)