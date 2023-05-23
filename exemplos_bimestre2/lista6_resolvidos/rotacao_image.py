#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html
"""

import os
import image


def rotacao_90(img: image.Image) -> image.Image:
    
    altura_original = img.get_height()
    largura_original = img.get_width()

    nova_altura = largura_original
    nova_largura = altura_original

    nova_imagem = image.EmptyImage(nova_largura, nova_altura)

    for lin in range(nova_altura):
        for col in range(nova_largura):
            pixel_antiga = img.get_pixel(lin, col)  #pixel com lin e col "invertidos"
            nova_imagem.set_pixel(col, lin, pixel_antiga)

    return nova_imagem


def rotacao(img: image.Image, angulo) -> image.Image:
    if angulo == 90:
        return rotacao_90(img)
    
    #else
    return img  #não altera

    ##TODO fazer p/ outros angulos (180 e 270)

##PROGRAMA PRINCIPAL

img = image.Image(os.path.join(os.getcwd(), "luther.jpg"))

win = image.ImageWin(max(img.getHeight(), img.getWidth()), max(img.getHeight(), img.getWidth()))

img = rotacao(img)

img.draw(win)

win.exitonclick()