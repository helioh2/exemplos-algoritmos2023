


def marcar_tudo_como_comprado(vetor):
    
    for pos in range(0, len(vetor)):
        if vetor[pos] is not None:
            vetor[pos] = vetor[pos] + " COMPRADO"



def multiplica_tudo_por_dois(vetor):

    for pos in range(0, len(vetor)):
        vetor[pos] = vetor[pos] * 2



lista_numeros = list(range(10, 1010, 10))
print(lista_numeros)
multiplica_tudo_por_dois(lista_numeros)
print(lista_numeros)



lista_compras = ["arroz", "feijao", "macarrao", "ovo", None, None]

marcar_tudo_como_comprado(lista_compras)

print(lista_compras)