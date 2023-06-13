



def somatorio(vetor) -> float:

    resultado = 0    # acumulador

    for pos in range(0, len(vetor)):
        resultado = resultado + vetor[pos]

    return resultado



def produtorio(vetor) -> float:

    resultado = 1    # acumulador

    for pos in range(0, len(vetor)):
        resultado = resultado * vetor[pos]

    return resultado



lista_numeros = list(range(10, 1010, 10))
print(lista_numeros)

despesas = [2323, 344, 565, 1212, 34]

total_despesas = somatorio(despesas)

print(total_despesas)


produto_despesas = produtorio(despesas)
print(produto_despesas)