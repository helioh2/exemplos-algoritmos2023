import turtle


def aplicar_regras(char):
    newstr = ""
    if char == 'A':
        newstr = 'B'   # Regra 1
    elif char == 'B':
        newstr = 'AB'  # Regra 2
    else:
        newstr = char    # nenhuma regra se aplica

    return newstr


def processa_string(string):
    newstr = ""
    for ch in string:
        newstr = newstr + aplicar_regras(ch)

    return newstr


def criar_sistema_L(num_iters, axioma):
    string_inicial = axioma
    string_final = ""
    for i in range(num_iters):
        string_final = processa_string(string_inicial)
        string_inicial = string_final

    return string_final

print(criar_sistema_L(10,"A"))


def desenha_sistema_L(tart, instrucoes, angulo, distancia):
    for cmd in instrucoes:
        if cmd == 'F':
            tart.forward(distancia)
        elif cmd == 'B':
            tart.backward(distancia)
        elif cmd == '+':
            tart.right(angulo)
        elif cmd == '-':
            tart.left(angulo)
        else:
            print('Erro:', cmd, 'é um comando desconhecido')



##PROGRAMA PRINCIPAL

def main():
    inst = criar_sistema_L(10,"FXF--FF--FF")   #create the string
    print(inst)
    t = turtle.Turtle()           #create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    desenha_sistema_L(t,inst,120,10)     
    wn.exitonclick()

main()