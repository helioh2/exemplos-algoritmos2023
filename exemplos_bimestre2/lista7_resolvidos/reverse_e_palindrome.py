


def reverse(palavra: str) -> str:
    
    n = len(palavra)
    inicio = n - 1  # se n=7, então inicio=6
    fim = -1

    resultado = ""

    for pos in range(inicio, fim, -1):

        caracter_atual = palavra[pos]

        resultado = resultado + caracter_atual

    # fim do for
    return resultado



def palindrome(palavra: str) -> bool:
    if reverse(palavra) == palavra:
        return True
    else:
        return False


def palindrome_v2(palavra: str) -> bool:
    if reverse(palavra) == palavra:
        return True  # se entrou aqui, o return termina a execução da função
    
    return False


def palindrome_v3(palavra: str) -> bool:
    return reverse(palavra) == palavra



def palindrome_sem_reverse(palavra: str) -> bool:
    
    n = len(palavra)
    inicio = 0
    fim = n//2 

    for pos in range(inicio, fim):

        pos_reverso = n - pos - 1

        if palavra[pos] != palavra[pos_reverso]:  ## condição de parada, não é palindrome
            return False    # termina a execução (não precisa checar o resto)
    
    return True   #se parou aqui, significa que nenhum caracter deu diferente




def f():
    return 1 + 2

print(f())

## EXEMPLOS / TESTES
assert reverse("") == ""
assert reverse("oi joao") == "oaoj io"
assert reverse("banana") == "ananab"
assert reverse("arara") == "arara"
assert reverse(".!.!?") == "?!.!."
print("passou nos testes")


print(reverse("oi joao"))

print(palindrome("banana"))
print(palindrome("arara"))

print(palindrome_sem_reverse("banana"))
print(palindrome_sem_reverse("arara"))