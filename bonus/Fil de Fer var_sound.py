import sfml as sf
import random
from functions_first import *
from functions_second import *


def get_fdf(tab2, step, img, vc):
    a = random.uniform(1, 2)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line])):
            x = col*step + step
            y = line*step + step
            z = -1/a * (int(tab2[line][col])) + random.uniform(0, vc.y)
            X = 0.5*x - 0.5*y + step*len(tab2)/2
            Y = z + (0.5/2)*x + (0.5/2)*y
            tab2[line][col] = sf.Vector3(X, Y, z)
    for line in range(0, len(tab2) - 1):
        for col in range(0, len(tab2[line])):
            c = color_line(tab2[line][col].z, tab2[line + 1][col].z, col, vc.x)
            lineas(tab2[line][col], tab2[line + 1][col], c, img)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line]) - 1):
            c = color_line(tab2[line][col].z, tab2[line][col + 1].z, col, vc.x)
            lineas(tab2[line][col], tab2[line][col + 1], c, img)


def main():
    file = check("fdf.fdf")
    tab = fdf_tab(file)
    xy = sf.Vector2(1920, 1080)
    step = int(xy.x / len(tab))
    clock = sf.Clock()
    son = sound("Harlem_Shake.wav")
    t = 0
    w = sf.RenderWindow(sf.VideoMode(xy.x, xy.y), "FDF", sf.Style.FULLSCREEN)
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent or \
                    sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        w.clear(sf.Color.BLACK)
        frame(clock, w)
        if t > 115:
            t = 0
        t = t + 1
        vars = sf.Vector2(sf.Mouse.get_position().x / 7.6, t)
        tab = fdf_tab(file)
        img = sf.Image.create(xy.x, xy.y, sf.Color.TRANSPARENT)
        get_fdf(tab, step, img, vars)
        tex = sf.Texture.from_image(img)
        spr = sf.Sprite(tex)
        w.draw(spr)
        w.display()
main()