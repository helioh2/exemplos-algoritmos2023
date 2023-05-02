import turtle
import random

wn = turtle.Screen()
alex = turtle.Turtle()

angulos = [10,67,93,-156,332,-40]

print(angulos)

for angulo in angulos:
    alex.forward(100)
    alex.left(angulo)

print("O pirata bebado virou", angulo, "graus por último")





dia_semana_inicio = int(input("Digite o dia da semana de inicio de ferias:"))
total_ferias = int(input("Digite o total de dias de férias:"))

dia_semana_retorno = (total_ferias + dia_semana_inicio)%7

print(dia_semana_retorno)





