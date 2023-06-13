
import turtle


def aplica_regras(caracter_atual: str) -> str:
    if caracter_atual == "X":
        return "X+YF++YF-FX--FXFX-YF+"
    elif caracter_atual == "Y":
        return "-FX+YFYF++YF+FX--FX-Y"
    else:
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


def desenha_sistema_L(tart: turtle.Turtle, axioma: str, num_iters: int):

    sistema = criar_sistema_L(axioma, num_iters)

    for indice in range(len(sistema)):
        caracter_atual = sistema[indice]

        if caracter_atual == "F":
            tart.forward(9)
        if caracter_atual == "B":
            tart.backward(9)
        elif caracter_atual == "-":
            tart.left(60)
        elif caracter_atual == "+":
            tart.right(60)
        
        

print(criar_sistema_L("FX", 6))

alex = turtle.Turtle()
wn = turtle.Screen()


desenha_sistema_L(alex, "FX", 6)