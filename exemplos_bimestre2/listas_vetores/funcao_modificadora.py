def dobro(lista: list):    # recebe uma referência a uma lista na memória
    """ (list) -> None
    Recebe uma lista referenciada por
    'lista' e sobreescreve cada
    elemento da lista com o dobro do
    seu valor.
    """
    for posicao in range(0, len(lista)):
        lista[posicao] = 2 * lista[posicao]
        

coisas = [2, 5, 9]
print(coisas)
dobro(coisas)   # passa a referência à lista 'coisas'
print(coisas)

## DICA: COPIE E COLE ESTE CÓDIGO NO Python Tutor PARA VER PASSO A PASSO
# https://pythontutor.com/python-debugger.html#mode=edit
