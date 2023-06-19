#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html
"""

import os
import image


def rotacao_90_a_esquerda(img: image.Image) -> image.Image:
    
    altura_original = img.get_height()
    largura_original = img.get_width()

    nova_altura = largura_original   #nova imagem tem altura e largura trocados
    nova_largura = altura_original

    nova_imagem = image.EmptyImage(nova_largura, nova_altura)
    print(nova_imagem.get_height())
    print(nova_imagem.get_width())

    for lin in range(altura_original):
        for col in range(largura_original):
            #pegadinha: img.get_pixel recebe na ordem x, y (col, lin)
            pixel_antiga = img.get_pixel(x=col, y=lin)  
            nova_imagem.set_pixel(x=lin, y=largura_original-col-1, pixel=pixel_antiga)  

    return nova_imagem


def rotacao_esquerda(img: image.Image, angulo) -> image.Image:
    if angulo == 90:
        return rotacao_90_a_esquerda(img)
    if angulo == 180:
        return rotacao_90_a_esquerda(rotacao_90_a_esquerda(img))  # é possível fazer de forma mais eficiente
    if angulo == 270:
        return rotacao_90_a_esquerda(rotacao_90_a_esquerda(rotacao_90_a_esquerda(img))) # é possível fazer de forma mais eficiente
                                     
    #else
    return img  #não altera

    ##TODO (por fazer) fazer p/ outros angulos (180 e 270)

##PROGRAMA PRINCIPAL

img = image.Image(os.path.join(os.getcwd(), "luther.jpg"))

win = image.ImageWin(max(img.getHeight(), img.getWidth()), max(img.getHeight(), img.getWidth()))

img = rotacao_esquerda(img, 270)

img.draw(win)

win.exitonclick()