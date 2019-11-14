from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
points = 0


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 5
        self.vy = 5
        self.ay = -1
        self.is_dead = False
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x > 800-self.r:
            self.vx = -self.vx
        if self.y > 600-self.r:
            self.vy = -0.9*self.vy
            if self.vy < self.y + self.r - 600:
                self.y = 600 - self.r
            print(self.vy)
            if self.vy < 10:
                self.is_dead = True
        self.x += self.vx
        self.y -= self.vy
        self.vy += self.ay
        self.set_coords()

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x)**2 + (obj.y - self.y)**2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    f2_power = 10
    f2_on = 0
    an = 1

    def __init__(self):
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    live = 1
    id_points = canv.create_text(30, 30, text=points, font='28')

    def __init__(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(20, 50)
        self.color = 'red'
        self.id = canv.create_oval(0, 0, 0, 0)
        self.vy = 2
        # self.new_target()
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self):
        global points
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        canv.delete(self.id)
        points += 1
        canv.itemconfig(self.id_points, text=points)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        self.y = self.y + self.vy
        if self.y >= 600-self.r:
            self.vy = -self.vy
        if self.y <= self.r:
            self.vy = -self.vy
        self.set_coords()


screen1 = canv.create_text(400, 300, text='', font='28')
gun = Gun()
bullet = 0


def new_game():
    global screen1, balls, bullet
    target1 = Target()
    target2 = Target()
    balls = []
    dead_balls = []
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targeting)
    target1.live = 1
    target2.live = 1
    canv.itemconfig(screen1, text='')
    while target1.live or target2.live or balls:
        target1.move()
        target2.move()
        for b in balls:
            b.move()
            if b.is_dead:
                dead_balls.append(b)
            if b.hit_test(target1) and target1.live:
                target1.live = 0
                canv.delete(target1.id)
                canv.itemconfig(screen1, text='')
                target1.hit()
            if b.hit_test(target2) and target2.live:
                target2.live = 0
                canv.delete(target2.id)
                canv.itemconfig(screen1, text='')
                target2.hit()
            if target2.live == 0 and target1.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                if bullet == 1:
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрел')
                elif bullet == 2 or bullet == 3 or bullet == 4:
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрела')
                else:
                    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                for j in balls:
                    balls.remove(j)
                    canv.delete(j.id)
        for j in dead_balls:
            balls.remove(j)
            canv.delete(j.id)
        dead_balls = []
        canv.update()
        time.sleep(0.03)
        gun.targeting()
        gun.power_up()
    time.sleep(3)
    canv.delete(Gun)
    root.after(750, new_game)


new_game()

tk.mainloop()
