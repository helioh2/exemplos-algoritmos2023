"""
Escreva uma função que, dada uma nota, retorna um string — o grau da nota de acordo com o esquema:


|  *Nota* | *Grau* |
|:-------:|:------:|
| >= 90   | A      |
| [80-90) | B      |
| [70-80) | C      |
| [60-70) | D      |
| < 60    | F      |

Os colchetes e os parênteses denotam intervalos fechados e abertos. Um intervalo fechado inclui o número enquanto um intervalo aberto o exclui. Logo, 79.99999 corresponde a grau C, mas 80 corresponde a grau B.

Seja xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

Teste sua função imprimindo o grau para cada elemento da lista. (Dica: use o for sem o range, diretamente pegando cada item da lista)

"""


def grau_da_nota(nota: float) -> str:

	if nota >= 90:
		return "A"
	elif nota >= 80 and nota < 90:
		return "B"
	elif nota >= 70 and nota < 80:
		return "C"
	elif nota >= 60 and nota < 70:
		return "D"
	else:
		return "F"


## PROGRAMA PRINCIPAL

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for nota in xs:
	print(grau_da_nota(nota))



"""
ALTERNATIVA:

def grau_da_nota(nota: float) -> str:
	if nota >= 90:
		return "A"
	if 80 <= nota < 90:   ##ATENÇÃO: isto é permitido no Python, mas não em outras linguagens!!
		return "B"
	if 70 <= nota < 80:
		return "C"
	if 60 <= nota < 70:
		return "D"
	#senão
	return "F"

PERCEBA QUE NÃO USEI ELIFS!!! A EXPLICAÇÃO PARA ISSO É QUE NO CORPO DE CADA IF
EU DOU UM RETURN. QUANDO EU DOU RETURN, A EXECUÇÃO DA FUNÇÃO É TERMINADA.
LOGO, EU NÃO PRECISARIA DO ELSE EMBUTIDO NO ELIF, POIS O CÓDIGO NÃO CHEGARÁ 
NO PRÓXIMO IF. POR EXEMPLO: SE nota=85, ELE VAI ENTRAR NO SEGUNDO IF E 
EXECUTAR A LINHA LOGO ABAIXO, QUE FAZ O RETURN. PORTANTO, ELE NÃO VAI 
TENTAR EXECUTAR O TERCEIRO IF NEM NADA QUE VEM APÓS ELE.

PERCEBA TAMBÉM QUE PARA A ÚLTIMA CONDIÇÃO ("ELSE") EU NÃO PRECISEI COLOCAR O
COMANDO ELSE (COLOQUEI SOMENTE UM COMENTÁRIO ESCRITO senão PARA MARCAR
A SEMÂNTICA/SIGNIFICADO). ISSO OCORRE POIS, SE A EXECUÇÃO NÃO ENTROU EM NENHUM IF,
ENTÃO NUNCA EXECUTOU UM RETURN. LOGO, A EXECUÇÃO DA FUNÇÃO CHEGARÁ OBRIGATORIAMENTE
NA LINHA 'return "F"'. 


"""