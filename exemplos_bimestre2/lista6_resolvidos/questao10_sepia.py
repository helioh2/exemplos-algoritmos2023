import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for lin in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, lin)

        newred = min(int(0.393 * p.getRed()+ 0.769 * p.getGreen() + 0.189 * p.getBlue()), 255) #transforma em int, e em seguida pega o mínimo entre o valor dado e 255 a fim de evitar valores maiores que 255
        newgreen = min(int(0.349 * p.getRed() + 0.686 * p.getGreen() + 0.168 * p.getBlue()), 255)
        newblue = min(int(0.272 * p.getRed()+ 0.534 * p.getGreen() + 0.131 * p.getBlue()), 255)

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, lin, newpixel)

img.draw(win)
win.exitonclick()