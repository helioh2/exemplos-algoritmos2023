

"""
Desenvolver um sistema-L.
"""

import turtle


def aplica_regras(caracter_atual: str) -> str:
    if caracter_atual == "X":
        return "X+YF+"
    elif caracter_atual == "Y":
        return "-FX-Y"
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


def desenha_sistema_L(tart: turtle.Turtle, sistema: str, angulo: float, distancia: int):

    for indice in range(len(sistema)):
        caracter_atual = sistema[indice]

        if caracter_atual == "F":
            tart.forward(distancia)
        if caracter_atual == "B":
            tart.backward(distancia)
        elif caracter_atual == "-":
            tart.left(angulo)
        elif caracter_atual == "+":
            tart.right(angulo)
        
        

# print(criar_sistema_L("F", 6))

alex = turtle.Turtle()
wn = turtle.Screen()

alex.speed(0)

alex.penup()
alex.backward(wn.window_width()/2+20)
alex.pendown()

sistema = criar_sistema_L("FX", 10)
print(sistema)
desenha_sistema_L(alex, sistema, 90, 9)

wn.exitonclick()