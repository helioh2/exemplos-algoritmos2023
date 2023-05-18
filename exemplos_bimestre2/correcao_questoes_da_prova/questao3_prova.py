"""
 Escreva uma função frutífera soma_pares_até(n), que recebe um número natural n 
 e retorna a soma de todos os números naturais pares até e incluindo n (se n for par). 
 A função deve ser escrita usando o laço de repetição ‘for’ com o padrão de acumulação; 
 ou seja, NÃO é permitido usar a fórmula de soma de P.A. 

Deve-se também deixar explícita a assinatura da função, ou seja, os tipos de dados de entrada e o tipo de dado de saída. Você pode fazer isso usando um comentário de código.
Exemplos de chamadas à função:  

soma_pares_até(0) => 0,  que retornaria o valor 0
soma_pares_até(10) => 0+2+4+6+8+10,  que retornaria o valor 30
soma_pares_até(13) => 0+2+4+6+8+10+12,  que retornaria o valor 42

Em seguida, no programa principal, chame a função três vezes -- uma vez para 10, 
outra para 100 e outra para 1001 -- e guarde o retorno de cada chamada em uma variável diferente.
"""


## Duas funções possíveis (ambas corretas):

def soma_pares_ate_com_passo(n: int) -> int:

    soma = 0

    for numero in range(0, n, 2):
        soma = soma + numero
    
    return soma


def soma_pares_ate_sem_passo(n: int) -> int:

    soma = 0

    for numero in range(0, n):
        if numero % 2 == 0:  #se número é par
            soma = soma + numero
    
    return soma

## PROGRAMA PRINCIPAL
soma_pares_ate = soma_pares_ate_com_passo  # configurando qual usaremos (opcional)

a = soma_pares_ate(10)
b = soma_pares_ate(100)
c = soma_pares_ate(1001)

# print(a)   # prints não foram pedidos (opcional)
# print(b)
# print(c)


"""
BREVE DISCUSSÃO SOBRE AS DUAS SOLUÇÕES: QUAL A MELHOR?

NESTE CASO, A PRIMEIRA OPÇÃO (USANDO O PASSO NO RANGE) É MAIS RECOMENDADO,
ELE EXECUTARÁ MENOS VEZES DO QUE A OUTRA SOLUÇÃO.
POR QUÊ? PORQUE A PRIMEIRA FUNÇÃO EXECUTARÁ O 'FOR' CERCA DE n/2 VEZES, POIS
ELE PULA DE 2 EM 2. JÁ A SEGUNDA FUNÇÃO EXECUTARÁ O 'FOR' EXARTAMENTE n+1 VEZES,
POIS ELE PULA DE UM EM UM, ENTRANDO NO 'FOR' ATÉ MESMO QUANDO O NUMERO É IMPAR.
"""