import turtle
import random

def estaNaTela(wn, tart):
    """
    Funções utilizadas:
        wn.window_width() recupera a largura da janela
        wn.window_height() recupera a altura da janela
        tart.xcor() recupera a posição x da tart na tela
        tart.ycor() recupera a posição y da tart na tela
    """
    limiteEsquerdo = - wn.window_width()/2
    limiteDireito = wn.window_width()/2
    limiteSuperior = wn.window_height()/2
    limiteInferior = -wn.window_height()/2

    x_tart = tart.xcor()
    y_tart = tart.ycor()

    estaDentro = True  
    if x_tart > limiteDireito or x_tart < limiteEsquerdo:
        estaDentro = False
    if y_tart > limiteSuperior or y_tart < limiteInferior:
        estaDentro = False

    return estaDentro




#PROGRAMA PRINCIPAL
alex = turtle.Turtle()
wn = turtle.Screen()

alex.shape('turtle')

contagem = 0  #inicialização

while estaNaTela(wn, alex):  ## dica ex4: contagem < 4
    moeda = random.randrange(0,2)
    if moeda == 0:              # cara
        alex.left(90)
    else:                      # coroa
        alex.right(90)

    alex.forward(50)

    # dica ex4: se not estaNaTela(wn, alex) -> contagem += 1; dar meia volta
    contagem += 1  #incremento (ex: 1 -> 2; 2 -> 3)

    print(contagem)

print(contagem)

wn.exitonclick()