


def raiz_quadrada_newton(n: float) -> float:
    aprox = 0.5 * n
    melhor = 0.5 * (aprox + n/aprox)
    while melhor != aprox:
        aprox = melhor
        melhor = 0.5 * (aprox + n/aprox)
    return aprox
	
    
print(raiz_quadrada_newton(10))