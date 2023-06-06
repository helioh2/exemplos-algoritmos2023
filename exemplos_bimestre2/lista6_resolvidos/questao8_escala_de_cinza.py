import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for lin in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, lin)

        media = (p.getRed() + p.getGreen() + p.getBlue())//3
        
        newpixel = image.Pixel(media, media, media)

        img.setPixel(col, lin, newpixel)

img.draw(win)
win.exitonclick()