from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
# Create window with size 800x600 pixels.
canv = Canvas(root, bg='white')
# Create active window with white background.
canv.pack(fill=BOTH, expand=1)
# Make active window have the same size with window.
# For counting points.
points = 0
x = 0
y = 0
vx = 0
vy = 0
r = 0
ball = 0

colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue'
]


# Create massive with ball's colors.

def move():
    global x, y, vx, vy
    canv.move(ball, vx, vy)
    x = x + vx
    y = y + vy
    if x <= r or x >= 800 - r:
        vx = - vx
    if y <= r or y >= 600 - r:
        vy = - vy
    root.after(2000, move)


# Create a function, which moves ball.

def new_ball():
    global ball, x, y, r, vx, vy
    canv.delete('ball')
    r = rnd(30, 50)
    x = rnd(100 - r, 800 - r)
    y = rnd(100 - r, 600 - r)
    ball = canv.create_oval(x - r, y - r,
                            x + r, y + r,
                            outline=choice(colors),
                            fill=choice(colors),
                            width=5, tag='ball')
    vx = rnd(-1, 1)
    vy = rnd(-1, 1)
    root.after(2000, new_ball)


# Create ball.

def click(event):
    global points, x, y
    if ((event.x - x) ** 2 +
        (event.y - y) ** 2) <= r ** 2:
        canv.delete('ball')
        canv.delete('points')
        points = points + 1
        canv.create_text(50, 50, text=str(points),
                         anchor=CENTER, font="Purisa",
                         tag='points')


# Show points.

new_ball()
canv.bind('<Button-1>', click)
mainloop()
