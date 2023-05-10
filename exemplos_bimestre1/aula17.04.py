import turtle

wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("lightgreen")


alex = turtle.Turtle()            # cria alex
tess = turtle.Turtle()            # cria tess
tess.color("red")

def desenha_quadrado(tartaruga: turtle.Turtle, lado: int):
    """
    Desenha um quadrado com tamanho de 'lado' usando uma 'tartaruga'.
    :param tartaruga
    :param lado
    """
    for i in range(4):
        tartaruga.forward(lado)
        tartaruga.left(90)


desenha_quadrado(alex, 70)  # chamada da função
desenha_quadrado(alex, 120)  # chamada da função
desenha_quadrado(tess, 70)

wn.exitonclick()
