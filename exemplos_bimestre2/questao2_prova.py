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



"""
CONDIÇÃO DE PARADA: n == 1
"""


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    while n != 1:  # funciona tb: while not(n == 1)
        print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n)                  # the last print is 1

seq3np1(3)
