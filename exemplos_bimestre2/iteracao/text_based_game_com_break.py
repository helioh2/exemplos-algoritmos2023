
"""
Programa: início de um text-based game (jogo baseado em texto)
"""

sala_atual = "uma sala azul"   # declarei a variável e inicializei com um valor
sala_anterior = None

# CONDIÇÃO DE PARADA??? NÃO TEM!!!

while True:   # loop infinito

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
            print("PARABÉNS, VC ACHOU A SAÍDA DO LABIRINTO!!")
            break   #quebra, interrompe o laço (loop)

        else:
            print("Você passou pela porta oeste... Vamos em frente!")
            sala_anterior = sala_atual
            sala_atual = "uma sala amarela"

    else:
        print("VOCÊ NÃO PODE FAZER ISSO!! TÁ DOIDO(A)?")

   
    print("Você está em", sala_atual)


print("FIM DO PROGRAMA")
## FIM DO PROGRAMA

