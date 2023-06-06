import turtle
import random


CORES = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "gold", "silver", "violet", "lime", "teal", "indigo", "maroon"]

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


def executa_tartatugas_bebadas(n: int, largura_janela: int, altura_janela: int):
    """
    n é a quantidade de tartarugas
    """
    wn = turtle.Screen()

    wn.setup(largura_janela, altura_janela)

    ## Criando lista de tartatugas:
    tarts = []
    for k in range(n):
        tart = turtle.Turtle(shape="turtle")
        tart.color(CORES[k%len(CORES)]) # pega cor da constante CORES (ver inicio do arquivo)
        
        posicao_x_inicial = random.randrange(-largura_janela//2+1, largura_janela//2)
        posical_y_inicial = random.randrange(-altura_janela//2+1, altura_janela//2)
        
        tart.penup()
        tart.goto(posicao_x_inicial, posical_y_inicial)
        tart.pendown()

        tarts.append(tart)


    while tarts:  # enquanto tarts não é uma lista vazia

        ## Para cada tartaruga, joga uma moeda e faz o movimento
        for i in range(len(tarts)):
            tart_atual = tarts[i]
            moeda = random.randrange(0,2)

            if moeda == 0:
                tart_atual.left(90)
            else:
                tart_atual.right(90)

            tart_atual.forward(50)

            if not estaNaTela(wn, tart_atual):
                tart_atual.backward(50)
                if moeda == 0:
                    tart_atual.right(90)
                else:
                    tart_atual.left(90)

        ## Após cada tartaruga se mover, verifica se alguma se colidiu com a outra:
        ## Se colidiram, remove da lista para que não andem mais

        tarts_a_remover = set()  # set é parecido com uma lista, mas não permite elementos repetidos
        ## a ideia aqui é encontrar os indices das tartarugas que colidiram para remover depois
        for i in range(len(tarts)):
            for j in range(i+1, len(tarts)):
                tart1 = tarts[i]
                tart2 = tarts[j]

                if colidiram(tart1, tart2):
                    tarts_a_remover.add(i)  # adiciona o indice das tarts i e j na lista de tarts a remover
                    tarts_a_remover.add(j)
        
        print(tarts_a_remover)
        print(tarts)
        
        # a remoção será feita criando-se uma nova lista sem incluir os que estiverem em tarts_a_remover
        new_tarts = []  
        for i in range(len(tarts)):
            if i not in tarts_a_remover:
                new_tarts.append(tarts[i])

        tarts = new_tarts


    wn.exitonclick()


## PROGRAMA PRINCIPAL
executa_tartatugas_bebadas(5, 400, 400)


