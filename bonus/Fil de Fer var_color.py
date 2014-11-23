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
            z = -1/a * (int(tab2[line][col])) + random.uniform(0, 0)
            X = 0.5*x - 0.5*y + step*len(tab2)/2
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
    file = check("fdf.fdf")
    tab = fdf_tab(file)
    width = 1920
    h = 1080
    step = int(width / len(tab))
    clock = sf.Clock()
    w = sf.RenderWindow(sf.VideoMode(width, h), "FDF", sf.Style.FULLSCREEN)
    w.framerate_limit = 25
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent or \
                    sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        var_color = sf.Mouse.get_position().x / 7.6
        w.clear(sf.Color.BLACK)
        frame(clock, w)
        tab = fdf_tab(file)
        img = sf.Image.create(width, h, sf.Color.TRANSPARENT)
        get_fdf(tab, step, img, var_color)
        tex = sf.Texture.from_image(img)
        spr = sf.Sprite(tex)
        w.draw(spr)
        w.display()
main()