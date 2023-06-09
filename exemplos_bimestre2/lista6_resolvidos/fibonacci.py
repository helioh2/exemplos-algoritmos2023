


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
        return   # interrompe / termina a execução da função
    
    a = 0   # anterior do anterior
    b = 1   # anterior

    print(a)  # primeiro elemento

    if n == 1:  # n < 2
        return
    
    print(b) # segundo elemento

    # a partir do terceiro elemento, faz um loop realizando a soma dos dois elementos atuais e reatribuições
    cont = 2
    while cont < n:
    # for cont in range(2, n):
        # aux = a   # guarda o valor de 'a' em uma variável auxiliar (temporária)
        # a = b     # variável 'a' recebe o valor da variável 'b'
        # b = aux + b   # faz a soma de 'b' mais o valor anterior de 'a', que havia sido armazenada na variável auxiliar
        
        b_antigo = b
        b = a + b
        a = b_antigo

        cont += 1

        print(b)


## PROGRAMA PRINCIPAL

fibonacci(8)