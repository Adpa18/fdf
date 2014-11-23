import sfml as sf
from functions_first import *


def get_fdf(tab2, step, img, color):
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line])):
            x = col*step + step
            y = line*step + step
            z = -1/2 * (int(tab2[line][col]))
            X = 0.5*x - 0.5*y + step*len(tab2)/2
            Y = z + (0.5/2)*x + (0.5/2)*y
            tab2[line][col] = sf.Vector3(X,Y,z)
    for line in range(0, len(tab2) - 1):
        for col in range(0, len(tab2[line])):
            lineas(tab2[line][col], tab2[line + 1][col], color, img)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line]) - 1):
            lineas(tab2[line][col], tab2[line][col + 1], color, img)


def main():
    file = check("fdf.fdf")
    tab = fdf_tab(file)
    width = 1920
    h = 1080
    step = int(width / len(tab))
    img = sf.Image.create(width, h, sf.Color.TRANSPARENT)
    get_fdf(tab, step, img, sf.Color.WHITE)
    tex = sf.Texture.from_image(img)
    spr = sf.Sprite(tex)
    w = sf.RenderWindow(sf.VideoMode(width, h), "FDF", sf.Style.FULLSCREEN)
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent or \
                    sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        w.clear(sf.Color.BLACK)
        w.draw(spr)
        w.display()
main()