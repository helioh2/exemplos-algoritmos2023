
"""
A           Axioma

A -> B      Regra 1 Mude A para B

B -> AB     Regra 2 Mude B to AB
"""















def aplica_regras(char: str) -> str:
    if char == "A":
        return "B"
    if char == "B":
        return "AB"
    #else
    return char

def processa_string(string: str) -> str:
    nova_string = ""
    for char in string:
        nova_string = nova_string + aplica_regras(char)
    return nova_string


def criar_sistema_L(axioma: str, num_iters: int) -> str:

    string_atual = axioma
    resultado = ""

    for i in range(num_iters):
        resultado = processa_string(string_atual)
        string_atual = resultado

    return resultado





#PROGRAMA PRINCIPAL E TESTES

assert criar_sistema_L("A", 3) == "BAB"
assert criar_sistema_L("A", 4) == "ABBAB"

print(criar_sistema_L("A",20))