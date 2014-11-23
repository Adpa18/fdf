import sfml as sf
import random


def color_line(z1, z2, x, var_color):
    ri = random.randint
    if sf.Mouse.is_button_pressed(sf.Mouse.LEFT):
        if z1 < 0 or z2 < 0:
            color = sf.Color(abs(x*13 - var_color), 255 - x*8, 255)
        else:
            color = sf.Color(255 - var_color, 255 - x*10, 126 - x*6)
    else:
        if z1 < 0 or z2 < 0:
            color = sf.Color(ri(128, 255), 50, 50)
        else:
            color = sf.Color(ri(10, 255), ri(10, 255), ri(10, 255))
    return (color)


def frame(clock, w):
    time1 = clock.elapsed_time
    sec = round(1/ time1.seconds, 2)
    time1 = clock.restart()
    txt1 = sf.Text("FPS : " + str(float(sec)))
    txt1.font = sf.Font.from_file("Candarab.ttf")
    txt1.character_size = 30
    txt1.style = sf.Text.BOLD
    txt1.color = sf.Color.RED
    w.draw(txt1)


def sound(file):
    buffer = sf.SoundBuffer.from_file(file)
    son = sf.Sound()
    son.buffer = buffer
    son.loop = True
    son.play()
    return (son)