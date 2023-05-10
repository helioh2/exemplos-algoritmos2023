"""
Desenhar um tabuleiro de xadrez com tamanho arbitrário (i.e., é possível
escolher seu tamanho) e par de cores arbitrários.
Ex: tabuleiro 400x400, cinca e preto
Ex: tabuleiro 600x600, azul e amarelo

Funções úteis (módulo Universe):
tela = criar_tela_base(altura: int, largura: int) -> pg.Surface
quadrado(lado: int, cor: str) -> pg.Surface
encima(imagem: pg.Surface, imagem: pg.Surface) -> pg.Surface
lado(imagem: pg.Surface, imagem: pg.Surface) -> pg.Surface
colocar_imagem_sobre_tela_e_mostrar(imagem: pg.Surface, x: int, y: int)
"""

from htdp_pt_br.universe import *


def padrao_xadrez(tamanho: int, cor1: str, cor2: str) -> pg.Surface:
    quadrado1 = quadrado(tamanho//8, cor1)
    quadrado2 = quadrado(tamanho//8, cor2)
    linha1 = lado(quadrado1, quadrado2)
    linha2 = lado(quadrado2, quadrado1)
    return encima(linha1, linha2)


def quadradao(tamanho: int, cor1: str, cor2: str) -> pg.Surface:
    return quatro_imagens(padrao_xadrez(tamanho, cor1, cor2))

def quatro_imagens(imagem: pg.Surface) -> pg.Surface:
    linha = lado(imagem, imagem)
    return encima(
        linha,
        linha
    )


def tabuleiro(tamanho: int, cor1: str, cor2: str) -> pg.Surface:
    return quatro_imagens(quadradao(tamanho, cor1, cor2))



tela = criar_tela_base(500, 500) 

tab1 = tabuleiro(400, "gray", "black")
tab2 = tabuleiro(200, "blue", "green")
tab3 = tabuleiro(50, "green", "white")
"""
Outros testes:

quadrado1 = quadrado(50, "blue")
quadrado2 = quadrado(50, "black")
print(type(quadrado1))

p1 = padrao_xadrez(400, "red", "black")

padrao_xadrez_vertical = encima(quadrado1, quadrado2)

circulo1 = circulo(70, "red")

circulos = quatro_imagens(circulo1)

quadrado_circulo = lado(circulo1, quadrado1)
"""

p1 = padrao_xadrez(400, "red", "black")
colocar_imagem_sobre_tela_e_mostrar(tab3, 500//2, 500//2)