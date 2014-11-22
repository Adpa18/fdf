import sfml as sf
import math
import sys
import os

def lineas(p1, p2, color, img):
    p1x = int(p1.x)
    p2.x = int(p2.x)
    p1.y = int(p1.y)
    p2.y = int(p2.y)
    tab = []
    if p2.x == p1.x:
        for x in range(p1.y, p2.y):
            img[p1.x, x] = color
            tab.append(sf.Vector2(int(p1x),int(x)))
        for x in range(p2.y, p1.y):
            img[p1.x, x] = color
            tab.append(sf.Vector2(int(p1x),int(x)))
    else:
        a = (p2.y-p1.y)/(p2.x-p1.x)
        b = p1.y - a*p1x
        while p2.x > p1x:
            y = a*p1x + b
            img[p1x,y] = color
            tab.append(sf.Vector2(int(p1x),int(y)))
            p1x = p1x + 0.5
        while p2.x < p1x:
            y = a*p1x + b
            img[p1x,y] = color
            tab.append(sf.Vector2(int(p1x),int(y)))
            p1x = p1x - 0.5
    return (tab)

def full(p1, p2, p3, img):
    tab1 = lineas(p1,p2, sf.Color.WHITE, img)
    tab2 = lineas(p1,p3, sf.Color.WHITE, img)
    tab3 = lineas(p2,p3, sf.Color.WHITE, img)
    for pos in range(0, len(tab3)):
        lineas(tab3[pos], tab2[pos], sf.Color.RED, img)

def main():
    width = 1000
    height = 1000
    p1 = sf.Vector2(100, 100)
    p2 = sf.Vector2(100, 200)
    p3 = sf.Vector2(200, 200)
    img = sf.Image.create(width, height, sf.Color.TRANSPARENT)
    full(p1, p2, p3, img)
    tex = sf.Texture.from_image(img)
    spr = sf.Sprite(tex)
    w = sf.RenderWindow(sf.VideoMode(width, height), "Fil De Fer")
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent:
                w.close()
        w.clear(sf.Color.BLACK)
        w.draw(spr)
        w.display()
main()