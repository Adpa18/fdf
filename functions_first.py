import sfml as sf
import sys


def lineas(p1, p2, color, img):
    p1x = int(p1.x)
    tab = []
    if p2.x == p1.x:
        for x in range(p1.y, p2.y):
            if p1x >= 0:
                img[p1.x, x] = color
        for x in range(p2.y, p1.y):
            if p1x >= 0:
                img[p1.x, x] = color
    else:
        a = (p2.y-p1.y)/(p2.x-p1.x)
        b = p1.y - a*p1x
        while p2.x > p1x:
            y = a*p1x + b
            if p1x >= 0 and y >= 0:
                img[p1x, y] = color
                tab.append(sf.Vector2(int(p1x), int(y)))
            p1x = p1x + 0.5
        while p2.x < p1x:
            y = a*p1x + b
            if p1x >= 0 and y >= 0:
                img[p1x, y] = color
                tab.append(sf.Vector2(int(p1x), int(y)))
            p1x = p1x - 0.5
    return (tab)


def fdf_tab(file):
    xyz = open(file, "r")
    lines = xyz.readlines()
    tab2 = xyz.readlines()
    for line in lines:
        tab = (line.split())
        tab2.append(tab)
    for y in range(0, len(tab2) - 1):
        if len(tab2[y]) != len(tab2[y + 1]):
            print("Error : the *.fdf file isn't a rectangular form.")
            sys.exit(0)
    return (tab2)


def check(default):
    if len(sys.argv) == 1:
        file = default
    elif len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print("Error : Please enter right syntax : fdf.py [file.fdf]")
        sys.exit(0)
    return (file)