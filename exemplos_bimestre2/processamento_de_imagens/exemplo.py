#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html
"""

import os
import image
import time


img = image.Image(os.path.join(os.getcwd(), "luther.jpg"))

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for lin in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, lin)

        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, lin, newpixel)


img.draw(win)
win.exitonclick()