
"""
VÁRIOS EXEMPLOS DE LOOP SIMPLES USANDO O WHILE
RETIRE O CÓDIGO DE DENTRO DAS ASPAS TRIPLAS PARA TESTAR
"""

"""
#Loop infinito e sem incremento:

contagem = 0   # inicialização da variável contagem com o valor inicial 0
while True:  # não há condição de parada, pois dá sempre True
    print(contagem)
"""

"""
#Loop infinito, mas com incremento:

contagem = 0     # inicialização da variável contagem com o valor inicial 0
while True:  # não há condição de parada, pois dá sempre True
    print(contagem)
    contagem += 1   # incremento do valor da variável contagem
"""


"""
# Colocando condição de continuidade até 1000 
# (ou seja, condição de parada é quando chega no 1001)

contagem = 0     # inicialização da variável contagem com o valor inicial 0
while contagem <= 1000: 
    print(contagem)
    contagem += 1      # incremento do valor da variável contagem
"""


"""
# Usando if... break dentro do while para fazer a condição de parada:

contagem = 0    # inicialização da variável contagem com o valor inicial 0
while True:
    print(contagem)
    contagem += 1     # incremento do valor da variável contagem
    if contagem > 1000:   # a condição de parada é implementada aqui. Entrará nesse if quando 'contagem' atingir o valor 1001
        break    # interrompe o loop

"""


"""
# Usando for (apenas para comparação):
# Perceba que o comando 'for' já embute o comando de incremento
# Perceba também que ele automaticamente já inicializa a variável
# de laço ('contagem') com o valor 0
# e cria a condição de parada (quando atinge '1000+1')

for contagem in range(0, 1000+1):
    print(contagem)
"""

