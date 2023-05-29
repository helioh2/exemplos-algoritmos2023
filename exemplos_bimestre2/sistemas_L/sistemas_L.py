

"""
Desenvolver um sistema-L.
"""

def aplica_regras(caracter_atual: str) -> str:
    if caracter_atual == "A":
        ## trocar por B
        # string[indice] = "B"  #não dá pra fazer isso com string, pois string é um tipo de dado imutável
        return "B"
    elif caracter_atual == "B":
        ## trocar por AB
        return "AB"
    else:
        ## nao troca nada
        return caracter_atual


def transforma(string: str) -> str:
    
    resultado = ""

    for indice in range(0, len(string)): # 0, 1, 2, 3...
        caracter_atual = string[indice]  # string[0], string[1], string[2]
        resultado = resultado + aplica_regras(caracter_atual)

    return resultado
#end transforma

def criar_sistema_L(axioma: str, num_iters: int) -> str:
    
    string_atual = axioma  # A -> B -> AB -> ...

    for k in range(num_iters):

        string_atual = transforma(string_atual)
    
    return string_atual



## TESTES (A IDEIA É QUE IRÁ PASSAR NOS TESTES QUANDO EU COMPLETAR A FUNÇÃO)
assert transforma("A") == "B"
assert transforma("B") == "AB"
assert transforma("ABBAB") == "BABABBAB"

print(transforma("ABBAB"))

assert criar_sistema_L("A", 6) == "ABBABBABABBAB"

print("OBA, PASSAMOS EM TODOS OS TESTES")


print(criar_sistema_L("A", 6))
# "ABBAB"
