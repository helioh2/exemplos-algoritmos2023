
"""
Programa: início de um text-based game (jogo baseado em texto) infinito,
ainda muito inicial, de forma que vc sempre entra em uma sala idêntica 
à anterior (um quarto azul)
"""



sala_atual = "uma sala azul"   # declarei a variável e inicializei com um valor
sala_anterior = None

# saiu = False  # inicializando a variavel com valor False
dentro = True

while dentro:  #alternativa: while not saiu (necessário inicializar e modificar a variável 'saiu')

    escolha = input("Escolha a porta pela qual vc vai passar (norte, sul, leste ou oeste): ")

    if escolha == "norte":

        print("Você passou pela porta norte.... O que haverá adiante?")
        sala_anterior = sala_atual
        sala_atual = "uma sala verde"

    elif escolha == "sul":

        print("Você passou pela porta sul... E agora?")
        sala_anterior = sala_atual
        sala_atual = "uma sala vermelha"

    elif escolha == "leste":

        print("Você passou pela porta leste... Vixi, e agora?")
        sala_anterior = sala_atual
        sala_atual = "uma sala roxa"

    elif escolha == "oeste":

        if sala_atual == "uma sala vermelha":
            ## SAIU DO LABIRINTO
            # saiu = True
            dentro = False
            print("PARABÉNS, VC ACHOU A SAÍDA DO LABIRINTO!!")
        else:
            print("Você passou pela porta oeste... Vamos em frente!")
            sala_anterior = sala_atual
            sala_atual = "uma sala amarela"

    else:
        print("VOCÊ NÃO PODE FAZER ISSO!! TÁ DOIDO?")

    if dentro:
        print("Você está em", sala_atual)


print("FIM DO PROGRAMA")
## FIM DO PROGRAMA
