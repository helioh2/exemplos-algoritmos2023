



def print_numeros_triangulares(n:int):

    i = 1  # valor inicial da variavel de laco
    while i <= n:
        ## quando i = 1
        #soma = 1

        ## quando i = 2
        #soma = 2+1 = 3

        ## quando i = 3
        #soma = 3+2+1 = 6

        numero_triangular = 0
        
        k = 1
        while k <= i:
            numero_triangular += k
            k += 1  # incrementa o k

        print(i, "\t", numero_triangular)

        i += 1   # incrementar


print_numeros_triangulares(10)
