


import random

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar(mensagem: str, alfabeto_cifracao: str) -> str:

    mensagem = mensagem.upper()  # converte mensagem para letras maiusculas
    resultado = ""

    for i in range(0, len(mensagem)):
        char = mensagem[i]
        ord_char = ord(char)
        indice_char = ord_char - 65
        novo_char = alfabeto_cifracao[indice_char]

        resultado += novo_char

    return resultado


def decifrar(mensagem: str, alfabeto_cifracao: str) -> str:

    mensagem = mensagem.upper()  # converte mensagem para letras maiusculas
    resultado = ""

    for i in range(0, len(mensagem)):
        char = mensagem[i]
        indice_char = alfabeto_cifracao.index(char)  #pega o indice do caracter no alfabeto de cifração
        novo_char = ALFABETO[indice_char]  # usa o indice no alfabeto normal

        resultado += novo_char

    return resultado



##TESTES:
assert cifrar("OLAMUNDO", "BCDEFGHIJKLMNOPQRSTUVWXYZA") == "PMBNVOEP"  # cifra que troca cada letra pela próxima no alfabeto

assert decifrar("PMBNVOEP", "BCDEFGHIJKLMNOPQRSTUVWXYZA") == "OLAMUNDO"

# lista_alfabeto = list(ALFABETO.strip())
# print(lista_alfabeto)
# random.shuffle(lista_alfabeto)
# cifra = "".join(lista_alfabeto)
# print(cifra)

assert cifrar("OLAMUNDO", "NILYRHDQJSUBGFAKWEOCPVMXZT") == "ABNGPFYA"
assert decifrar("ABNGPFYA", "NILYRHDQJSUBGFAKWEOCPVMXZT") == "OLAMUNDO"

