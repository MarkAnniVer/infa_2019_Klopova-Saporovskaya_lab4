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

def motion(vx, vy):
    global a
    canv.move(a, vx, vy)
    root.after(1, motion)
	
def new_ball():
    global x, y, r, a
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    a = canv.create_oval(x - r, y - r, x + r, y + r, fill = choice(colors), width = 0)
    motion(3, 3)
    root.after(1000, new_ball)
# Function creates ball with radius r
# and (x,y) coordinates of the centre
# with color from colors[].
# After 1000 ms delete previous ball 
# and create new one.

def click(event):
    if((x - event.x)**2 + (y - event.y)**2 <= r**2):
        global points
        points += 1
# Function counts points.

def print_points(event):
    global points
    print(points)
# Print points.
	
new_ball()
# Call new_ball() function.
canv.bind('<Button-1>', click)
# Call click function after noticing
# button is pressed.
root.bind("<Key>", print_points)
mainloop()
# Giving information about events 
# to widgets.