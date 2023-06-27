
import sys



def maior(lista: list[int]):

    if len(lista) == 0:
        return None

    maior_atual = -99999999999  ## inicializa com menor número possível

    for pos in range(0, len(lista)):
        item = lista[pos]

        if item > maior_atual:
            ## troca o valor do maior_atual pelo item
            maior_atual = item
    
    return maior_atual
    


def maior_v2(lista: list[int]):

    if len(lista) == 0:   # se a lista for vazia, retorna None
        return None

    maior_atual = lista[0]

    for pos in range(1, len(lista)):
        item = lista[pos]

        if item > maior_atual:
            ## troca o valor do maior_atual pelo item
            maior_atual = item
    
    return maior_atual
    


## TESTES/EXEMPLOS

v1 = [10, 20, 70, 4, 15]

assert maior_v2(v1) == 70
assert maior_v2([-100, -50, -1]) == -1
assert maior_v2([]) == None