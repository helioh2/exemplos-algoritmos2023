

"""
Desenvolver um sistema-L.
"""

import turtle


def aplica_regras(caracter_atual: str) -> str:
    if caracter_atual == "F":
        return "F-F++F-F"
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


    historico_posicoes_salvas = []

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
        elif caracter_atual == '[':
            historico_posicoes_salvas.append([tart.heading(), tart.xcor(), tart.ycor()])
            ## heading() retorna a direção da tart, xcor() retorna posição x e ycor() retorna posição y
            print(historico_posicoes_salvas)
        elif caracter_atual == ']':
            posicao_e_sentido = historico_posicoes_salvas.pop()   #remove item do final da lista e o retorna 
            print(posicao_e_sentido)
            print(historico_posicoes_salvas)
            tart.setheading(posicao_e_sentido[0])  # altera a direção da tart para a que estava no histórico 
            tart.setposition(posicao_e_sentido[1], posicao_e_sentido[2])  # altera x e y da tart para a que estava no histórico
        else:
            print('Erro:', caracter_atual, 'é um comando desconhecido')
        
        

print(criar_sistema_L("F", 6))

alex = turtle.Turtle()
alex.speed(0)
wn = turtle.Screen()

inst = "F[-FFFF[-FFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFFFFFFFFFF[-FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFFFFFF[-FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X]+FFFF[-FF[-F[-X]+X]+F[-X]+X]+FF[-F[-X]+X]+F[-X]+X"
alex.setposition(0,-200)
alex.left(90)
desenha_sistema_L(alex, inst, 30, 2)


wn.exitonclick()