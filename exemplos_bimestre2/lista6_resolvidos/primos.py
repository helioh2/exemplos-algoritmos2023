


"""
Um numero eh primo se ele for divisivel
apenas por 1 e por ele mesmo.

O que eh divisivel: quando vc divide um numero
por outro e o resto da zero
"""



def eh_primo(x: int) -> bool:
    
    ## x // n

    n = x // 2  #ex; se for x=13, entao n=6

    while n != 1 and x%n != 0:  #   not (n == 1 or x % n == 0)
        # enquando n!=1 e x nao eh dividivel por n, continua testando
        n = n - 1

    if n == 1: # testei todos e nao foi divisivel por nenhum
        return True
    else:
        return False

## TESTES:

# print(eh_primo(4))  # --> False
# print(eh_primo(13))  # --> True

assert eh_primo(4) == False
assert eh_primo(13) == True
assert eh_primo(182) == False
assert eh_primo(104729) == True

print(eh_primo(13))
print(eh_primo(12))

print("OS TESTES PASSARAM")

