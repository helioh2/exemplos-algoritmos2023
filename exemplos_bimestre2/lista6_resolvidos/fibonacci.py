


def fibonacci(n: int):
    """
    Imprime na tela a sequência de Fibonacci até o nº elemento.
    Ex: quando n=1
        0
        quando n=2
        0 1
        quando n=3
        0 1 1
        quando n=8
        0 1 1 2 3 5 8 13
    """

    if n < 1:
        return

    a = 0
    b = 1

    print(a)  # primeiro elemento

    if n < 2:
        return
    
    print(b)

    cont = 2
    while cont < n:
        aux = a
        a = b
        b = aux + b
        cont += 1
        print(b)


## PROGRAMA PRINCIPAL

fibonacci(8)