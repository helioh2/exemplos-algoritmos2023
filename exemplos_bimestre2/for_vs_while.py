

def someAteComFor(limite):
    soma = 0  #VALOR INICIAL, DECLARANDO A VARIÁVEL
    for numero in range(1, limite+1):
        soma = soma + numero

    return soma

print(someAteComFor(4))

print(someAteComFor(1000))



"""
ESTRUTURA DO while:

while <condicao>:
    <corpo>

Explicação:

enquanto condição for verdadeira:
    executa as instruções dentro (no corpo) do while
"""

def someAteComWhile(limite):
    """ Retorna a soma de 1+2+3 ... n """

    soma  = 0
    numero = 1  #declarando a variável 'numero' e atribuindo o valor inicial 1
    while numero <= limite:  # note que o numero vai até (e inclusive) o limite. Ex: se limite for 1000, ele ainda vai entrar no while quando numero=1000
        soma = soma + numero
        numero = numero + 1  #incremento "na mão". O 'for' faz isso automaticamente. O 'while' não!
    return soma

print(someAteComWhile(4))   # 1+2+3+4 = 10

print(someAteComWhile(1000))  # 1+2+3+...+1000
