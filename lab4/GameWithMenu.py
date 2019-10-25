from tkinter import *

window = Tk()
label = Label(window)


def save_as():
    label['text'] = 'Сохранить как'


def save():
    label['text'] = 'Сохранить'


def new():
    label['text'] = 'Создать'


menu = Menu(window)
submenu = Menu(window)
window.config(menu=menu)
submenu.add_command(label="Сохранить как", command=save_as)
submenu.add_command(label="Сохранить", command=save)
menu.add_cascade(label="Файл", menu=submenu)
menu.add_command(label="Создать", command=new)
label.pack()
window.mainloop()