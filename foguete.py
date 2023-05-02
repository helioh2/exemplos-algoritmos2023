#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" CONTEÚDO EXTRA À DISCIPLINA, NÃO DADO EM AULA"""

"""
Fazer uma animação de um foguete que aparece descendo a partir
do topo da tela e termina pousando no chão (parte inferior da tela)

Funções úteis (módulo Universe):
tela = criar_tela_base(altura: int, largura: int) -> pg.Surface
carregar_imagem(nome_arquivo_imagem: str, largura_imagem: int, altura_imagem: int) -> pg.Surface
colocar_imagem(imagem_frente: pg.Surface, imagem_fundo: pg.Surface, x: int, y: int) -> pg.Surface
big_bang(estado_inicial, funcao_tick: function, funcao_desenha: function, cor_fundo: str, etc...)
"""

from htdp_pt_br.universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (400, 400)
tela = criar_tela_base(LARGURA, ALTURA)

L_FOGUETE = 100
A_FOGUETE = 100
IMG_FOGUETE = carregar_imagem('foguete.png', L_FOGUETE, A_FOGUETE)    #os.path.join('', 'cat1.png')

# X = 200  #numero magico
X = LARGURA // 2


'''==================='''
'''# Definições de dados: '''

''' Foguete é Int[0,ALTURA] 
interp. representa a posicao y do foguete em pixels
Exemplos:
'''
F_INICIAL = 0
F_MEIO = ALTURA//2
F_FINAL = ALTURA
'''Template:
def fn_para_foguete(y):
    if y > ALTURA or y < 0:
        return "Foguete invalido"
    else:
        ... y
'''



'''===================='''
''' Funções: '''

'''
desce: Foguete -> Foguete
Faz o foguete descer 3 pixels no eixo y, se não estiver no chao
'''
def desce(y):
    if y > ALTURA or y < 0:
        raise ValueError("ERRO: A altura do foguete não pode ser menor que 0 nem maior que a altura máxima.")
    else:
        if y >= ALTURA - 2:
            return ALTURA
        else:
            return y + 3


'''
desenha: Foguete -> Imagem
Desenha foguete na tela
'''
def desenha(y):
    img = colocar_imagem(IMG_FOGUETE, tela, X, y - A_FOGUETE + 28)
    return img


''' ================= '''
''' Main (Big Bang):
'''

''' Foguete -> Foguete '''
''' inicie o mundo com main()'''
def main():
    big_bang(F_INICIAL,
             a_cada_tick=desce, \
             desenhar=desenha,
             cor_fundo=Cor("blue"))



main()