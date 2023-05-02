"""
Estrutura do FOR em pseudocódigo (português):

para cada valor NOME_DA_VARIAVEL_DE_LACO entre INICIO e FIM:
	... FAZ ALGUMA COISA


Tradução para Python:

for NOME_DA_VARIAVEL_DE_LACO in range(INICIO, FIM + 1):
    # ... Faz alguma coisa
"""


"""
Programa: imprimir todos os números da P.G. na base 2:
"""
def imprime_exp_2(n):
    for i in range(0, n+1):
        print("2**", i, "=", 2**i, sep="")


""" NUMEROS PARES DE O A 100
para cada valor x entre 0 e 100 passo 2:
	escreva x
"""
def mostra_pares(n):
    for x in range(0, n+1, 2):
        print(x)


""" CONTAGEM REGRESSIVA:
para cada valor cont entre 10 e 0 passo -1:
	escreva x
"""
def contagem_regressiva(n):
    for cont in range(n, -1, -1):
        print(cont)


## PROGRAMA PRINCIPAL
# imprime_exp_2(5)
# mostra_pares(1000)
contagem_regressiva(100)