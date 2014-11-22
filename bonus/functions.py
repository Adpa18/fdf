import sfml as sf
import random


def lineas(p1, p2, color, img):
    p1x = int(p1.x)
    tab = []
    if p2.x == p1.x:
        for x in range(p1.y, p2.y):
            if p1x >= 0 and y >= 0:
                img[p1.x, x] = color
                tab.append(sf.Vector2(int(p1x),int(x)))
        for x in range(p2.y, p1.y):
            if p1x >= 0 and y >= 0:
                img[p1.x, x] = color
                tab.append(sf.Vector2(int(p1x),int(x)))
    a = (p2.y-p1.y)/(p2.x-p1.x)
    b = p1.y - a*p1x
    while p2.x > p1x:
        y = a*p1x + b
        if p1x >= 0 and y >= 0:
            img[p1x, y] = color
            tab.append(sf.Vector2(int(p1x),int(y)))
        p1x = p1x + 0.5
    while p2.x < p1x:
        y = a*p1x + b
        if p1x >= 0 and y >= 0:
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
    if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
        if z1 < 0 or z2 < 0:
            color = sf.Color(abs(x*13 - var_color), 255 - x*8, 255)
        else:
            color = sf.Color(255 - var_color, 255 - x*10, 126 - x*6)
    else:
        if z1 < 0 or z2 < 0:
            color = sf.Color(random.randint(10,255),random.randint(10,255),random.randint(10,255))
            color = sf.Color(random.randint(128,255),50,50)
        else:
            color = sf.Color(random.randint(10,255),random.randint(10,255),random.randint(10,255))
    return (color)