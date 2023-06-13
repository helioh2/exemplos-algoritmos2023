def dobro(lista: list):
    """ (list) -> list
    Recebe uma lista referenciada por
    'lista' e cria e retorna uma nova
    lista em que cada elemento e' o
    dobro do valor correspondente
    na lista original.
    """
    nova_lista = []
    for pos in range(0, len(lista)):
       novo_elemento = 2 * lista[pos]
       nova_lista.append(novo_elemento)
    return nova_lista


#PROGRAMA PRINCIPAL
coisas = [2, 5, 9]
print(coisas)
coisas = dobro(coisas) # perceba que coisas recebe a nova lista retornada pela função dobro
print(coisas)
