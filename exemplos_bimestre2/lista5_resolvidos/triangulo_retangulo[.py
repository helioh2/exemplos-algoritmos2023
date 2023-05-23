
def eh_triangulo_retangulo_raiz(a: float, b: float, c: float) -> bool:

    if (a > b and a > c):
        hipo = a
        cat1 = b
        cat2 = c
    elif (b > a and b > c):
        hipo = b
        cat1 = a
        cat2 = c
    elif (c > a and c > b):
        hipo = c
        cat1 = a
        cat2 = b

    soma_quadrado_dos_catetos = cat1**2 + cat2**2

    if (abs(soma_quadrado_dos_catetos - hipo**2) < 0.000001):
        return True
    
    #else
    return False


def eh_triangulo_retangulo_chique(a: float, b: float, c: float) -> bool:

    lados = [a, b, c]  # cria lista com os lados
    hipo = max(lados)  # pega o valor máximo dos lados
    hipo_index = lados.index(hipo)  # pega o índice do lado maior (hipo) na lista
    lados.pop(hipo_index) # remove a hipotenusa, sobrando apenas os dois catetos

    soma_quadrado_dos_catetos = sum(lado**2 for lado in lados)  #faz a somatório do quadrado dos lados da lista (os catetos)

    return abs(soma_quadrado_dos_catetos - hipo**2) < 0.000001  # é possível retornar diretamente, sem fazer o if, pois a comparação já retorna o valor booleano desejado



##TESTES
assert eh_triangulo_retangulo_raiz(4,3,5) #dá erro se resultado retornar False
assert eh_triangulo_retangulo_raiz(3,4,5)
assert eh_triangulo_retangulo_raiz(3,5,4)
assert eh_triangulo_retangulo_raiz(5,4,3)

assert not eh_triangulo_retangulo_raiz(4,4,4) #dá erro se resultado retornar True
assert not eh_triangulo_retangulo_raiz(1,2,3)
assert not eh_triangulo_retangulo_raiz(3,1,2)


assert eh_triangulo_retangulo_chique(4,3,5)
assert eh_triangulo_retangulo_chique(3,4,5)
assert eh_triangulo_retangulo_chique(3,5,4)
assert eh_triangulo_retangulo_chique(5,4,3)

assert not eh_triangulo_retangulo_chique(4,4,4)
assert not eh_triangulo_retangulo_chique(1,2,3)
assert not eh_triangulo_retangulo_chique(3,1,2)