
"""
12. Três critérios devem ser levados em conta para identificar anos bissextos:
O ano deve ser divisível por 4;
Se o ano puder ser dividido por 100, NÃO é um ano bissexto, a menos que:
      O ano também é divisível por 400. Neste caso, é um ano bissexto.
Escreva uma função que receba um ano como parâmetro e retorne True se o ano for bissexto, False caso contrário.
"""


def eh_bissexto(ano: int) -> bool:
    
    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:
                return True
            #else
            return False
    
        #else
        return True
    
    #else
    return False

## TESTES:
assert not eh_bissexto(2023)  #dá erro se resultado retornar True
assert not eh_bissexto(500)
assert not eh_bissexto(600)

assert eh_bissexto(400)  # dá erro se resultado retornar False
assert eh_bissexto(800)
assert eh_bissexto(1200) 
assert eh_bissexto(1600)
assert eh_bissexto(2024)
assert eh_bissexto(1988)

# mais exemplos em: https://mundoeducacao.uol.com.br/matematica/anos-bissextos.htm


# Explicação sobre a ausência de 'else': ver arquivo correcao_questoes_da_prova/questao4_prova.py