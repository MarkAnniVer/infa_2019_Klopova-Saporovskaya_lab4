from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
play = Button(canv, text="Change", width=15, height=3)
play.place(x=200, y=200)
points = 0
x = 7 * [0]
y = 7 * [0]
vx = 7 * [0]
vy = 7 * [0]
r = 7 * [0]
a = 7 * [0]
ball = 7 * [0]
colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue'
]


def new_ball():
    global ball, x, y, r, vx, vy
    play.destroy()
    for i in range(7):
        canv.delete(ball[i])
    for i in range(7):
        print(i)
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
        canv.update()
    root.after(2000, new_ball)


play.pack(side='top')
canv.pack(fil=BOTH, expand=1)
play['command'] = new_ball
root.mainloop()
