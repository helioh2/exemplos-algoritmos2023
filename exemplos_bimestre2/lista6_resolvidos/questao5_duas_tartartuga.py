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



def colidiram(tart1, tart2) -> bool:
    """
    Colisão aproximada de duas tartarugas.
    A ideia é definir um limite de proximidade. Se os valores nos eixos x e y das 
    duas tartrugas estiver abaixo desse limite, considera-se que colidiram.
    """
    limite_proximidade = 20
    return (abs(tart1.xcor() - tart2.xcor()) < limite_proximidade 
        and abs(tart1.ycor() - tart2.ycor()) < limite_proximidade)


#PROGRAMA PRINCIPAL


wn = turtle.Screen()

largura_janela = 400
altura_janela = 400

wn.setup(largura_janela, altura_janela)

alex = turtle.Turtle()
beth = turtle.Turtle()

alex.shape('turtle')
alex.color("blue")
beth.shape('turtle')
beth.color("red")

## Gerando as posições x e y aleatórias para alex e beth:
x_inicial_alex = random.randrange(-largura_janela//2+1, largura_janela//2)
y_inicial_alex = random.randrange(-altura_janela//2+1, altura_janela//2)
x_inicial_beth = random.randrange(-largura_janela//2+1, largura_janela//2)
y_inicial_beth = random.randrange(-altura_janela//2+1, altura_janela//2)

alex.penup()
alex.goto(x_inicial_alex, y_inicial_alex)
alex.pendown()

beth.penup()
beth.goto(x_inicial_beth, y_inicial_beth)
beth.pendown()

while True: 
    moeda_alex = random.randrange(0,2)
    moeda_beth = random.randrange(0,2)
    if moeda_alex == 0:              # cara
        alex.left(90)
    else:                      # coroa
        alex.right(90)
    if moeda_beth == 0:              # cara
        beth.left(90)
    else:                      # coroa
        beth.right(90)

    alex.forward(50)
    beth.forward(50)

    if colidiram(alex, beth):  #ver definição da função colidiram
        break

    if not estaNaTela(wn, alex):
        alex.backward(50)
        if moeda_alex == 0:
            alex.right(90)
        else:
            alex.left(90)

    if not estaNaTela(wn, beth):
        beth.backward(50)
        if moeda_beth == 0:
            beth.right(90)
        else:
            beth.left(90)

    


wn.exitonclick()