from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
# Create window with size 800x600 pixels.
canv = Canvas(root, bg = 'white')
# Create active window with white background.
canv.pack(fill = BOTH, expand = 1)
# Make active window have the same size with window.
# For counting points.
points = 0

colors = [
   'red',
   'orange',
   'yellow',
   'green',
   'blue'
   ]
# Create massive with ball's colors.

def move():
    global x1, y1, vx1, vy1
    canv.move(ballA, vx1, vy1)
    x1 = x1 + vx1
    y1 = y1 + vy1
    root.after(50, move)
    if x1 <= r1 or x1 >= 800 - r1:
        vx1 = - vx1
    if y1 <= r1 or y1 >= 600 - r1:
        vy1 = - vy1
# Create a function, which moves ball.

def new_ball():
    global ballA, x1, y1, r1, vx1, vy1
    canv.delete('ballA')
    r1 = rnd(30, 50)
    x1 = rnd(100 - r1, 800 - r1)
    y1 = rnd(100 - r1, 600 - r1)
    ballA = canv.create_oval(x1 - r1, y1 - r1,
                             x1 + r1, y1 + r1, 
							 outline = choice(colors), 
							 fill = choice(colors), 
							 width = 5, tag = 'ballA')
    vx1 = rnd(-1, 1)
    vy1 = rnd(-1, 1)
    move()
    root.after(2000, new_ball)
# Create ball.
	
def click(event):
    global points, x1, y1
    if ((event.x - x1) ** 2 + 
	    (event.y - y1) ** 2) <= r1 ** 2:
        canv.delete('ballA')
        canv.delete('points')
        points = points + 1
        canv.create_text(50, 50, text = str(points),
                 		 anchor = CENTER, font = "Purisa", 
						 tag = 'points')
# Show points.

new_ball()
canv.bind('<Button-1>', click)
mainloop()