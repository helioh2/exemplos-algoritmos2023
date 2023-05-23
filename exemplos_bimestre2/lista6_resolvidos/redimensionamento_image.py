#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html
"""

import math
import os
import image


def redimensionar_imagem(img: image.Image, proporcao: float) -> image.Image:
    
    altura_original = img.get_height()
    largura_original = img.get_width()

    nova_altura = math.floor(altura_original * proporcao)  #math.floor arredonda o numero para baixo
    nova_largura = math.floor(largura_original * proporcao)

    nova_imagem = image.EmptyImage(nova_largura, nova_altura)

    for lin in range(nova_altura):
        for col in range(nova_largura):
            lin_antiga = math.floor(lin / proporcao) #cálculo reverso à proporção, para pegar o pixel do original
            col_antiga = math.floor(col / proporcao)
            pixel_antiga = img.get_pixel(col_antiga, lin_antiga)
            nova_imagem.set_pixel(col, lin, pixel_antiga)

    return nova_imagem


##PROGRAMA PRINCIPAL

img = image.Image(os.path.join(os.getcwd(), "luther.jpg"))

proporcao = 0.5

win = image.ImageWin(img.getWidth()*proporcao, img.getHeight()*proporcao)

img = redimensionar_imagem(img, proporcao)

img.draw(win)

win.exitonclick()