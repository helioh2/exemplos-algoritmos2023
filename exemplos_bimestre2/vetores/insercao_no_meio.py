


def inserir_no_meio(vetor, item, indice):

    n = len(vetor)
    if vetor[n-1] != None:
        print("ERRO: LISTA CHEIA")
        return  # termina
    
    for pos in range(n-2, indice-1, -1):
        vetor[pos+1] = vetor[pos]

    vetor[indice] = item



def remover_do_meio(vetor, indice):

    n = len(vetor)
    for pos in range(indice, n-1):

        if vetor[pos] == None:  # se encontrar vazio, nada mais a fazer
            return   #cabou

        vetor[pos] = vetor[pos+1]
    
    vetor[n-1] = None



n = 6
vetor = [10, 30, 40, 50, 60, None]

inserir_no_meio(vetor, 20, 1)

print(vetor)

#vetor = [10, 20, 30, 40, 50, 60]


remover_do_meio(vetor, 2)

print(vetor)



vetor2 = [10, None, None]

remover_do_meio(vetor2, 0)

print(vetor2)