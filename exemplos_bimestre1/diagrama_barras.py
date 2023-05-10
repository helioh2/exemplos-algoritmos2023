import turtle


def desenhaBarra(tartaruga, x):
    tartaruga.left(90)
    tartaruga.forward(x)
    tartaruga.right(90)
    tartaruga.forward(15)
    tartaruga.right(90)
    tartaruga.forward(x)
    tartaruga.left(90)


def desenhaGraficoDeBarra(tartaruga, xs):
    for x in xs:
        desenhaBarra(alex, x)


wn = turtle.Screen()

alex = turtle.Turtle()
alex.speed(1)
alex.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]
zs = [100, 20, 9, 43, 28, 49, 209, 182]

desenhaGraficoDeBarra(alex, xs)
alex.goto(0,0)
alex.color("blue")
desenhaGraficoDeBarra(alex, zs)


wn.exitonclick()



