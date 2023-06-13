



def busca(vetor, item) -> int:
    """
    Busca sequencial / busca linear
    """
    n = len(vetor)
    for indice in range(0, n):
        valor = vetor[indice]  # acessando o valor dentro do vetor naquele indice
        if valor == item:
            return indice   # retorna o indice e termina a exec da função
    # fim do for
    return None  # não encontrou




## PROGRAMA PRINCIPAL

lista_compras = ["arroz", "feijao", "macarrao", "ovo", None, None]
item = "macarrao"

#TESTE
assert busca(lista_compras, item) == 2
assert busca(lista_compras, "arroz") == 0
assert busca(lista_compras, "detergente") == None