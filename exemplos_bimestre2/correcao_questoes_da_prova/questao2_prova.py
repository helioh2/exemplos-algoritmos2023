"""
Escreva na tela "Executou o for x vezes", 1000 vezes
Ex:
Executou o for 1 vezes
Executou o for 2 vezes
"""


for cont in range(1, 1000+1):
    if cont == 1:
        print("Executou o for", cont, "vez")
    else:
        print("Executou o for", cont, "vezes")

