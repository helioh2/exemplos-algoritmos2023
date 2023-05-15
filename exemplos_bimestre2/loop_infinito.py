
"""
Programa: início de um text-based game (jogo baseado em texto) infinito,
ainda muito inicial, de forma que vc sempre entra em uma sala idêntica 
à anterior (um quarto azul)
"""



sala_atual = "um quarto azul"


while True:
    escolha_porta = input("Escolha uma porta para entrar (norte, sul, leste ou oeste):")

    if escolha_porta == "norte":
        print("Você passou pela porta norte... O que haverá adiante?")
    elif escolha_porta == "sul":
        print("Você passou pela porta sul... O que haverá adiante?")
    elif escolha_porta == "leste":
        print("Você passou pela porta leste... O que haverá adiante?")
    elif escolha_porta == "oeste":
        print("Você passou pela porta oeste... O que haverá adiante?")
    else:
        print("PORTA INVÁLIDA!!")

    print("Você se encontra em", sala_atual)