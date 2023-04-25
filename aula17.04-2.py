

def quadrado(x):
    y = x * x
    oba = "Olá"
    return y

# print(oba)
# print(y)

# z = quadrado(10)
# print(z)


def quadrado_sem_multiplicacao(x: int) -> int:
    """
    Int -> Int  # assinatura
    """
    soma = 0
    for i in range(x):
        soma = soma + x

    return soma  

#Exemplos de uso:
v = quadrado_sem_multiplicacao(0)  # 0
print(v)
v = quadrado_sem_multiplicacao(1)  # 1
print(v)
v = quadrado_sem_multiplicacao(2)  # 2 + 2 = 4
print(v)
v = quadrado_sem_multiplicacao(3)  # 3 + 3 + 3 = 9
print(v)

