import sfml as sf
import math
import sys
import random
import winsound as ws
import threading
from threading import Thread
import time
from functions import *
from decimal import *


def get_fdf(file, step, img, var_color, t):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    a = random.uniform(1,2)
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line])):
            x = col*step + step
            y = line*step + step
            z = -1/a * (int(tab2[line][col])) + random.uniform(0,t)
            X = 0.5*x - 0.5*y + step*10
            Y = z + (0.5/2)*x + (0.5/2)*y
            tab2[line][col] = sf.Vector3(X,Y,z)
    for line in range(0, len(tab2) - 1):
        for col in range(0, len(tab2[line])):
            color = color_line(tab2[line][col].z, tab2[line + 1][col].z, col, var_color)
            lineas(tab2[line][col], tab2[line + 1][col], color, img)
    for line in range(0, len(tab2)):
        for col in range(0, len(tab2[line]) - 1):
            color = color_line(tab2[line][col].z, tab2[line][col + 1].z, col, var_color)
            lineas(tab2[line][col], tab2[line][col + 1], color, img)


def check():
    if len(sys.argv) == 1:
        file = "fdf.fdf"
    elif len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print("Error : Please enter right syntax : fdf.py [file.fdf]")
        sys.exit(0)
    return (file)


def frame(clock, w):
    time1 = clock.elapsed_time
    sec = 1 / time1.seconds
    time1 = clock.restart()
    txt1 = sf.Text("Framerate :" + str(Decimal(sec).quantize(Decimal('.01'),
    rounding=ROUND_HALF_UP)))
    txt1.font = sf.Font.from_file("Candarab.ttf")
    txt1.character_size = 30
    txt1.style = sf.Text.BOLD
    txt1.color = sf.Color.RED
    w.draw(txt1)

def main():
    file = check()
    lenght = get_fdf_len(file)
    width = 1920
    height = 1080
    step = int(width / lenght)
    t = 0
    clock = sf.Clock()
    w = sf.RenderWindow(sf.VideoMode(width, height), "Fil De Fer", sf.Style.FULLSCREEN)
    w.framerate_limit = 25
    buffer = sf.SoundBuffer.from_file("Harlem_Shake.wav")
    son = sf.Sound()
    son.buffer = buffer
    son.loop = True
    son.play()
    while w.is_open:
        for event in w.events:
            if type(event) is sf.CloseEvent or \
                    sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
                w.close()
        w.clear(sf.Color.BLACK)
        frame(clock, w)
        t = t + 1
        if t > 115:
            t = 0
        var_color = sf.Mouse.get_position().x / 7.6
        img = sf.Image.create(width, height, sf.Color.TRANSPARENT)
        get_fdf(file, step, img, var_color, t)
        tex = sf.Texture.from_image(img)
        spr = sf.Sprite(tex)
        w.draw(spr)
        w.display()
main()