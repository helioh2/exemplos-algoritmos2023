

def cifrar(mensagem: str, deslocamento: int) -> str:

    mensagem = mensagem.upper()  # converte mensagem para letras maiusculas
    resultado = ""

    for i in range(0, len(mensagem)):
        char = mensagem[i]
        ord_char = ord(char)
        indice_char = ord_char - 65
        indice_novo_char = (indice_char + deslocamento) % 26
        novo_char = chr(indice_novo_char + 65)

        resultado += novo_char

    return resultado


def decifrar(mensagem: str, deslocamento: int) -> str:
    return cifrar(mensagem, -deslocamento)   # é só cifrar com deslocamento invertido


##TESTES
assert cifrar("OLAMUNDO", 1) == "PMBNVOEP"
assert decifrar("PMBNVOEP", 1) == "OLAMUNDO"

assert cifrar("OLAMUNDO", 2) == "QNCOWPFQ"
assert decifrar("QNCOWPFQ", 2) == "OLAMUNDO"