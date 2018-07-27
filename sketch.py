from PApplet import *
from math import sin, cos


def setup():
    size(500, 500)
    background(128, 64, 0)


t = 0
x, y = 250, 250
r = 100


def draw():
    global t
    background(128, 64, 0)
    t += 0.1
    p1 = (x + r * cos(t), y + r * sin(t))
    p2 = (x - r * cos(t), y - r * sin(t))
    line(p1[0], p1[1], p2[0], p2[1])


def user_event(event):
    global y, x
    if event.type == pg.KEYDOWN:
        if event.key == ord(','):
            y -= 10
        if event.key == ord('o'):
            y += 10
        if event.key == ord('a'):
            x -= 10
        if event.key == ord('e'):
            x += 10


dApplet.set_setup(setup)
dApplet.set_draw(draw)
dApplet.set_user_event(user_event)

dApplet.run_scetch()
