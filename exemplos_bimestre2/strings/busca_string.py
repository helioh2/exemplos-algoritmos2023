




def busca(string: str, caracter_procurado: str) -> int:
    
    encontrei = False

    pos = 0
    while pos < len(string) and not encontrei:  # encontrei == False

        caracter_atual = string[pos]

        if caracter_atual == caracter_procurado:
            encontrei = True
        else:
            pos += 1  #incrementar
    # fim do while

    if encontrei == True:
        return pos
    else:
        return None



def busca2(string: str, caracter_procurado: str, inicio: int) -> int:
    
    encontrei = False

    pos = inicio
    while pos < len(string) and not encontrei:  # encontrei == False

        caracter_atual = string[pos]

        if caracter_atual == caracter_procurado:
            encontrei = True
        else:
            pos += 1  #incrementar
    # fim do while

    if encontrei == True:
        return pos
    else:
        return None


##TESTES/EXEMPLOS

assert busca("banana", "a") == 1
assert busca("banana", "c") == None
assert busca("melancia", "i") == 6
assert busca("", "i") == None
print("PASSOU NOS TESTES")

# print(busca("melancia", "i"))

# print(busca2("banana", "a", 2))


def print_todas_ocorrencias(palavra: str, caracter_procurado: str):
    
    inicio = 0
    pos_ultima = busca2(palavra, caracter_procurado, inicio)

    while pos_ultima != None:
        print(pos_ultima)
        inicio = pos_ultima + 1
        pos_ultima = busca2(palavra, caracter_procurado, inicio)


## chamada da função:
# print_todas_ocorrencias("banana", "a")
print_todas_ocorrencias("otorrinolaringologista", "o")