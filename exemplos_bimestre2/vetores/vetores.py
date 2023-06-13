

# def adiciona_no_final(vetor: list, qtde: int, item):
    
#     vetor[qtde] = item
#     qtde += 1   #inseri 1  (incrementa a quantidade)
#     return qtde



def adiciona_no_final(vetor: list, item):

    ## descobrir qual a primeira posição vazia
    indice = 0
    
    esta_dentro_do_vetor = indice < len(vetor)
    while esta_dentro_do_vetor and vetor[indice] != None:
        indice += 1   # andando "pra frente"

    ## fora do while

    if indice < len(vetor):
        ## inserir
        vetor[indice] = item
    else:
        print("ERRO: LISTA CHEIA")





#PROGRAMA PRINCIPAL
n = 10
lista_compras = [None]*n
# qtde = 0

# qtde = adiciona_no_final(lista_compras, qtde, "arroz")
# print(lista_compras)
# qtde = adiciona_no_final(lista_compras, qtde, "feijao")
# print(lista_compras)

n = 5
lista_compras = [None]*n
adiciona_no_final(lista_compras, "arroz")
adiciona_no_final(lista_compras, "feijao")
adiciona_no_final(lista_compras, "macarrao")
adiciona_no_final(lista_compras, "carne")
adiciona_no_final(lista_compras, "detergente")

print(lista_compras)

adiciona_no_final(lista_compras, "ovo")
adiciona_no_final(lista_compras, "banana")


