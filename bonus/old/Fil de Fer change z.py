import sfml as sf
import math
import sys

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

def get_fdf_len(file):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    return (len(tab2))

def color_line(z1, z2):
    if z1 != 0 or z2 != 0:
        color = sf.Color.BLUE
    else:
        color = sf.Color.WHITE
    return (color)

def get_fdf(file, step, img, pos):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line])):
            x = col*step + step
            y = line*step + step
            z = -1/pos * (int(tab2[line][col]))
            X = 0.5*x - 0.5*y + step*10
            Y = z + (0.5/2)*x + (0.5/2)*y
            tab2[line][col] = sf.Vector3(X,Y,z)
    for line in range(0, len(tab2) - 1):
        for col in range(0, len(tab2[line])):
            color = color_line(tab2[line][col].z, tab2[line + 1][col].z)
            lineas(tab2[line][col], tab2[line + 1][col], color, img)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line]) - 1):
            color = color_line(tab2[line][col].z, tab2[line][col + 1].z)
            lineas(tab2[line][col], tab2[line][col + 1], color, img)

def main():
    sys.path.append("C:\\Users\\Adrien\\Google Drive\\InstallIgraph")
    file = "fdf.fdf"
    lenght = get_fdf_len(file)
    width = 1500
    height = 752
    step = int(width / lenght)
    # step = 15
    pos = 0.5
    img = sf.Image.create(width, height, sf.Color.TRANSPARENT)
    get_fdf(file, step, img, pos)
    tex = sf.Texture.from_image(img)
    spr = sf.Sprite(tex)
    spr.position = 0, 0
    w = sf.RenderWindow(sf.VideoMode(width, height), "Fil De Fer")
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent:
                w.close()
            if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        if sf.Keyboard.is_key_pressed:
            if sf.Keyboard.is_key_pressed(sf.Keyboard.C):
                if pos >= 0.5:
                    a = 0.1
                elif pos <= -0.5:
                    a = -0.1
                if pos <= 2 and pos > 1.5:
                    pos = -2
                elif pos >= -2 and pos < -1.5:
                    pos = 2
                if (pos >= 0.5 and pos <= 2) or (pos <= -0.5 and pos >= -2):
                    pos = pos + a
                    img = sf.Image.create(width, height, sf.Color.TRANSPARENT)
                    get_fdf(file, step, img, pos)
                    tex = sf.Texture.from_image(img)
                    spr = sf.Sprite(tex)
        w.clear(sf.Color.BLACK)
        w.draw(spr)
        w.display()
main()