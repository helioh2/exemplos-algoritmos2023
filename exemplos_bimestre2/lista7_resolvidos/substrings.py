


def conta_substrings(string: str, substring: str) -> int:

    n = len(string)  #tamanho da string
    m = len(substring)   #tamanho da substring

    if m == 0:
        return 0

    indice_substring = 0
    contagem_substrings = 0

    for i in range(0, n):
        caracter_atual = string[i]
        
        if caracter_atual == substring[indice_substring]:
            indice_substring += 1  # se encontrou caracter, incrementa indice da substring

            if indice_substring == m:   # encontrou substring
                indice_substring = 0    # "reseta" indice da substring para começar a encontrar outra
                contagem_substrings += 1   # incrementa contagem, pois encontrou uma

        else:
            indice_substring = 0  #"reseta" indice da substring pois não encontrou

    return contagem_substrings  # retorna contagem



def remove_primeira_ocorrencia_substring(string: str, substring: str) -> str:

    n = len(string)  #tamanho da string
    m = len(substring)   #tamanho da substring

    if m == 0:
        return string

    indice_substring = 0
    resultado = ""
    achou = False

    for i in range(0, n):
        caracter_atual = string[i]
        
        if not achou and caracter_atual == substring[indice_substring]:
            indice_substring += 1  # se encontrou caracter, incrementa indice da substring

            if indice_substring == m:   # encontrou substring
                indice_inicio_da_substring = i - indice_substring + 1
                resultado = resultado[:indice_inicio_da_substring]   # remove da string resultado tudo o que havia entre o inicio da substring e o indice atual i
                achou = True
                continue  #ignorar restante do corpo do for, voltando imediatamente para a cabeça do 'for' (para evitar linha 58)
        else:
            indice_substring = 0  #"reseta" indice da substring pois não encontrou

        resultado += caracter_atual  #adiciona caracter atual ao resultado
    
    return resultado 


##TESTES
assert conta_substrings("abababababacaxi", "ab") == 5
assert conta_substrings("abababababacaxi", "abac") == 1
assert conta_substrings("abababababcaxi", "abac") == 0  # esse caso daria erro se não tivesse o else das linhas 25 e 26
assert conta_substrings("abababababacaxi", "be") == 0
assert conta_substrings("", "be") == 0
assert conta_substrings("abababababacaxi", "") == 0



assert remove_primeira_ocorrencia_substring("abababababacaxi", "ab") == "ababababacaxi"
assert remove_primeira_ocorrencia_substring("cxzabcbabababacaxi", "aba") == "cxzabcbbabacaxi"



