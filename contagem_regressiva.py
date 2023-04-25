


from htdp_pt_br.universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (50, 50)
tela = criar_tela_base(LARGURA, ALTURA)


'''===================='''
''' Funções: '''


def decrementa(cont: int) -> int:
    """
    Int -> Int
    """
    if cont > 0:
        return cont - 1
    else:
        return 0

# Testes de decrementa
assert decrementa(10) == 9
assert decrementa(0) == 0


def desenha(cont: int) -> pg.Surface:
    """
    Int -> pg.Surface
    """
    fonte = pg.font.SysFont("monospace", 40)
    return colocar_imagem(texto(str(cont), fonte, "red"), tela, LARGURA//2, ALTURA//2)

''' ================= '''
''' Main (Big Bang):
'''

''' Int -> Int '''
''' inicie o mundo com main()'''
def main():
    big_bang(10, 
             frequencia=1,
             a_cada_tick=decrementa,
             desenhar=desenha)
    

main()