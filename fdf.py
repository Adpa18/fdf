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
            tab2[line][col] = sf.system.Vector3(X,Y,z)
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
    img = sf.graphics.Image.create(width, h, sf.graphics.Color.TRANSPARENT)
    get_fdf(tab, step, img, sf.graphics.Color.WHITE)
    tex = sf.graphics.Texture.from_image(img)
    spr = sf.graphics.Sprite(tex)
    w = sf.graphics.RenderWindow(sf.window.VideoMode(width, h), "FDF", sf.window.Style.FULLSCREEN)
    while w.is_open:
        for event in w.events:
            if type(event) is sf.window.Event.CLOSED or sf.window.Keyboard.is_key_pressed(sf.window.Keyboard.ESCAPE):
                w.close()
        w.clear(sf.graphics.Color.BLACK)
        w.draw(spr)
        w.display()
main()
