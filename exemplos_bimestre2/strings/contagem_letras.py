

"""
Programa que recebe uma string e um caracter e retorna
quantas vezes aquele caracter aparece na string
"""


def contar_caracter(string: str, caracter_procurado: str) -> int:
    contagem = 0  # inicializando a variavel contagem

    for indice in range(0, len(string)):  # indice < len(string)?
        caracter_atual = string[indice]

        if caracter_atual == caracter_procurado: #achou 1
            ## somar 1 na contagem
            contagem += 1
    ## fim do for

    return contagem



##TESTES / "POR EXEMPLO:"
assert contar_caracter("banana", "a") == 3
assert contar_caracter("melancia", "a") == 2
assert contar_caracter("otorrinolaringologista", "o") == 5
print("PASSOU NOS TESTES")
print(contar_caracter("otorrinolaringologista", "o"))


x = contar_caracter("banana", "a")
print(x)