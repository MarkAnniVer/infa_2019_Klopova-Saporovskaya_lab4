from tkinter import *
from random import randrange as rnd, choice
import time
import numpy as np

root = Tk()
root.geometry('800x600')
# Create window with size 800x600 pixels.
canv = Canvas(root, bg='white')
# Create active window with white background.
canv.pack(fill=BOTH, expand=1)
# Make active window have the same size with window.
# For counting points.h
points = 0
x = 7 * [0]
y = 7 * [0]
vx = 7 * [0]
vy = 7 * [0]
xs = 7 * [0]
ys = 7 * [0]
vxs = 7 * [0]
vys = 7 * [0]
r = 7 * [0]
a = 7 * [0]
ball = 7 * [0]
square = 7 * [0]
colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue'
]


# Create massive with ball's colors.

def move_ball():
    global x, y, vx, vy
    for i in range(7):
        canv.move(ball[i], vx[i], vy[i])
        x[i] = x[i] + vx[i]
        y[i] = y[i] + vy[i]
        if x[i] <= r[i] or x[i] >= 800 - r[i]:
            vx[i] = - vx[i]
        if y[i] <= r[i] or y[i] >= 600 - r[i]:
            vy[i] = - vy[i]
    root.after(int(1000 / 24), move_ball)


# Create a function, which moves ball.

def new_ball():
    global ball, x, y, r, vx, vy
    for i in range(7):
        canv.delete(ball[i])
    for i in range(7):
        r[i] = rnd(30, 50)
        x[i] = rnd(100 - r[i], 800 - r[i])
        y[i] = rnd(100 - r[i], 600 - r[i])
        ball[i] = canv.create_oval(x[i] - r[i], y[i] - r[i],
                                   x[i] + r[i], y[i] + r[i],
                                   outline=choice(colors),
                                   fill=choice(colors),
                                   width=5, tag='ball[i]')
        vx[i] = rnd(-10, 10)
        vy[i] = rnd(-10, 10)
        # move_ball()
    root.after(2000, new_ball)


# Create ball.

def move_square():
    global xs, ys, vxs, vys
    for i in range(7):
        canv.move(square[i], vxs[i], vys[i])
        xs[i] = xs[i] + vxs[i]
        ys[i] = ys[i] + vys[i]
        if xs[i] <= a[i] or xs[i] >= 800 - a[i]:
            vxs[i] = - vxs[i]
        if ys[i] <= a[i] or ys[i] >= 600 - a[i]:
            vys[i] = - vys[i]
    root.after(int(1000 / 24), move_square)


# Create a function, which moves ball.

def new_square():
    global square, xs, ys, a, vxs, vys
    for i in range(7):
        canv.delete(square[i])
    for i in range(7):
        a[i] = rnd(30, 50)
        xs[i] = rnd(100 - a[i], 800 - a[i])
        ys[i] = rnd(100 - a[i], 600 - a[i])
        square[i] = canv.create_rectangle(xs[i] - a[i] / 2, ys[i] - a[i] / 2,
                                          xs[i] + a[i] / 2, ys[i] + a[i] / 2,
                                          outline=choice(colors),
                                          fill=choice(colors),
                                          width=5, tag='square[i]')
        vxs[i] = rnd(-10, 10)
        vys[i] = rnd(-10, 10)
        # move_square()
    root.after(2000, new_square)


# Create square.

def click_ball(event):
    global points, x, y
    for i in range(7):
        if ((event.x - x[i]) ** 2 +
                (event.y - y[i]) ** 2) <= r[i] ** 2:
            canv.delete(ball[i])
            canv.delete('points')
            points = points + 1
            canv.create_text(50, 50, text=str(points),
                             anchor=CENTER, font="Purisa",
                             tag='points')


# Show points.

def click_square(event):
    global points, xs, ys
    for i in range(7):
        if ((event.x - xs[i]) ** 2 +
                (event.y - ys[i]) ** 2) <= a[i] ** 2:
            canv.delete(square[i])
            canv.delete('points')
            points = points + 1
            canv.create_text(50, 50, text=str(points),
                             anchor=CENTER, font="Purisa",
                             tag='points')


# Show points.

new_ball()
new_square()
move_ball()
move_square()
canv.bind('<Button-3>', click_ball)
canv.bind('<Button-1>', click_square)
mainloop()
