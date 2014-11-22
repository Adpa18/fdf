import sfml as sf
import math
import sys
import random


def lineas(p1, p2, color, img):
    p1x = int(p1.x)
    if p1x < 0 or p2.x < 0 or p1.y < 0 and p2.y < 0:
        return (0)
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
            img[p1x, y] = color
            tab.append(sf.Vector2(int(p1x),int(y)))
            p1x = p1x + 0.5
        while p2.x < p1x:
            y = a*p1x + b
            img[p1x, y] = color
            tab.append(sf.Vector2(int(p1x),int(y)))
            p1x = p1x - 0.5
    return (tab)


def get_fdf_len(file):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    return (len(tab2))


def color_line(z1, z2, x, var_color):
    ri = random.randint
    if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
        if z1 < 0 or z2 < 0:
            color = sf.Color(abs(x*13 - var_color), 255 - x*8, 255)
        else:
            color = sf.Color(255 - var_color, 255 - x*10, 126 - x*6)
    else:
        if z1 < 0 or z2 < 0:
            color = sf.Color(ri(10, 255), ri(10, 255), ri(10, 255))
            color = sf.Color(ri(128, 255), 50, 50)
        else:
            color = sf.Color(ri(10, 255), ri(10, 255), ri(10, 255))
    return (color)


def get_fdf(file, step, img, vc):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    a = random.uniform(1,2)
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line])):
            print(tab2[line][col])
            # if isinstance(tab2[line][col], int) == False:
            #     print("Error : Please, the *.fdf have to contain only integer.")
            #     sys.exit(0)
            x = col*step + step
            y = line*step + step
            z = -1/a * (int(tab2[line][col])) + random.uniform(0, 0)
            X = 0.5*x - 0.5*y + step*10
            Y = z + (0.5/2)*x + (0.5/2)*y
            tab2[line][col] = sf.Vector3(X, Y, z)
    for line in range(0, len(tab2) - 1):
        for col in range(0, len(tab2[line])):
            c = color_line(tab2[line][col].z, tab2[line + 1][col].z, col, vc)
            lineas(tab2[line][col], tab2[line + 1][col], c, img)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line]) - 1):
            c = color_line(tab2[line][col].z, tab2[line][col + 1].z, col, vc)
            lineas(tab2[line][col], tab2[line][col + 1], c, img)


def main():
    if len(sys.argv) == 1:
        file = "fdf.fdf"
    elif len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print("Error : Please, enter right syntax : fdf.py [file.fdf]")
        sys.exit(0)
    lenght = get_fdf_len(file)
    wi = 1920
    h = 1080
    step = int(wi / lenght)
    #step = 1
    w = sf.RenderWindow(sf.VideoMode(wi, h), "Fil De Fer", sf.Style.FULLSCREEN)
    w.framerate_limit = 25
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent:
                w.close()
            if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        var_color = sf.Mouse.get_position().x / 7.6
        img = sf.Image.create(wi, h, sf.Color.TRANSPARENT)
        get_fdf(file, step, img, var_color)
        tex = sf.Texture.from_image(img)
        spr = sf.Sprite(tex)
        w.clear(sf.Color.BLACK)
        w.draw(spr)
        w.display()
main()