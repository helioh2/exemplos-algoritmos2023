
"""
Problema: remover todas as vogais de uma string
"""

def remover_vogais(string: str) -> str:
    
    vogais = "aeiouAEIOU"
    resultado = ""  #acumulador

    for pos in range(0, len(string)):

        char = string[pos]

        if not(char in vogais):  # if not (char == "a" or char=="b"....)
            resultado = resultado + char

    # fora do for
    return resultado


print(remover_vogais("banana"))

### TESTES / EXEMPLOS DE USO

print(remover_vogais("compsci"))  # -> "cmpsc"
print(remover_vogais("aAbEefIijOopUus"))  # -> "bfjps"


## TESTES AUTOMATIZADOS:
## assert <chamada da funcao> == <resultado esperado>
assert remover_vogais("compsci") == "cmpsc"
assert remover_vogais("aAbEefIijOopUus") == "bfjps"

    