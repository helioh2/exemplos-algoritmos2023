"""
Escreva uma função frutífera que, dada uma temperatura em graus
celsius, retorna uma string que informa o quão quente está

|  Temperatura |     Nivel    |
|:------------:|:------------:|
| >= 40        | Pelando      |
| [27-40)      | Quente       |
| [18-27)      | Agradável    |
| [10-18)      | Friozinho    |
| [0-10)       | Frio         |
| < 0          | Congelante   |

"""


def nivel_temperatura(temp: float) -> str:
    """ Float -> String """  ## assinatura
    if temp >= 40:
        return "Pelando"
    elif temp >= 27 and temp < 40:
        return "Quente"
    elif temp >= 18 and temp < 27:
        return "Agradável"
    elif temp >= 10 and temp < 18:
        return "Friozinho"
    elif temp >= 0 and temp < 10:
        return "Frio"
    else:  # caso contrário (temp < 0)
        return "Congelante"

"""Função não-frutífera = PROCEDIMENTO"""
def nivel_temperatura_v2(temp: float):
    """ Float -> _"""  ## assinatura
    if temp >= 40:
        print("Pelando")
    elif temp >= 27 and temp < 40:
        print("Quente")
    elif temp >= 18 and temp < 27:
        print("Agradável")
    elif temp >= 10 and temp < 18:
        print("Friozinho")
    elif temp >= 0 and temp < 10:
        print("Frio")
    else:  # caso contrário (temp < 0)
        print("Congelante")


##PROGRAMA PRINCIPAL (MAIN)

#Testes (exemplos)
nivel1 = nivel_temperatura(30)  # -> "Quente"
nivel2 = nivel_temperatura(50)  # -> "Pelando"
nivel3 = nivel_temperatura(0) # -> Frio

print("O nível para a temperatura 30 é ", nivel1)
print("O nível para a temperatura 50 é ", nivel2)
print("O nível para a temperatura 0 é ", nivel3)