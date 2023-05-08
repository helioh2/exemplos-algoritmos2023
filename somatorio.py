"""
Criar uma função frutífera que recebe dois números (inicio
e fim) e retorna o somatório dos números entre
o inicio (inclusive) e o fim (inclusive) 

"""

""" Int, Int -> Int"""
def somatorio(inicio: int, fim: int):
    
    soma = 0  # acumulador

    for k in range(inicio, fim + 1)  #intervalo [inicio, fim+1)
        soma = soma + k  # incrementando o acumulador

    return soma

#Programa principal


a = somatorio(0, 10)  # -> 0 + 0 + 1 + 2 + 3 +... + 10
b = somatorio(15, 18)  # -> 0 + 15 + 16 + 17 + 18 = 66
c = somatorio(0, 0)  # -> 0
d = somatorio(2, 1)  # -> 0

print(a)
print(b)
print(c)
print(d)