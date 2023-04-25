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