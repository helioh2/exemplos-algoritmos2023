
"""
Problema: remover todas as vogais de uma string
"""

def remover_vogais(string: str) -> str:
    
    vogais = "aeiouAEIOU"
    resultado = ""  #acumulador

    for idx in range(0, len(string)):

        char = string[idx]

        if not(char in vogais):  # if not (char == "a" or char=="b"....)
            resultado = resultado + char

    # fora do for
    return resultado




### TESTES / EXEMPLOS DE USO

print(remover_vogais("compsci"))  # -> "cmpsc"
print(remover_vogais("aAbEefIijOopUus"))  # -> "bfjps"


## TESTES AUTOMATIZADOS:
## assert <chamada da funcao> == <resultado esperado>
assert remover_vogais("compsci") == "cmpsc"
assert remover_vogais("aAbEefIijOopUus") == "bfjps"

    