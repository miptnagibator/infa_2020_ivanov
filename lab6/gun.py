from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.g = 2.5

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

    def Move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if self.x + self.r > 800:
            self.vx = -0.5 * self.vx
            self.x = 799 - self.r
        if self.y + self.r >= 600:
            self.vy = int(-0.3 * self.vy)
            self.vx = 0.7 * self.vx
            self.y = 600 - self.r
        if abs(self.vy) < 2 and self.y > 599 - self.r:
            self.vy = 0
            self.vx = 0
            self.g = 0
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.g

    def draw_ball(self):
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def delete_ball(self):
        canv.delete(self.id)

    def ball_stop(self):
        if self.vx == 0 and self.vy == 0:
            if self.live == 0:
                return True
            else:
                self.live -= 1
                return False
        else:
            return False

    def hittest(self, obj):
        if math.sqrt(abs(self.x - obj.GetPosX()) ** 2 + abs(self.y - obj.GetPosY()) ** 2) < self.r + obj.GetRadius():
            return True


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 1
        self.an = 0
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        new_ball.r = 3 + self.f2_power
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def PowerUp(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.vy = rnd(-4, 4)
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text='', font='28')
        self.NewTarget()

    def Move(self):
        if self.y - self.r < 50:
            self.vy = - self.vy
        if self.y + self.r >= 500:
            self.vy = -self.vy
        self.y -= self.vy

    def DrawTarget(self):
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def DeleteTarget(self):
        canv.delete(self.id)

    def NewTarget(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(100, 400)
        r = self.r = rnd(25, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def GetPosX(self):
        return self.x

    def GetPosY(self):
        return self.y

    def GetRadius(self):
        return self.r

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points

    def GetScore(self):
        return self.points

    def GetIDPoints(self):
        return self.id_points


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.NewTarget()
    t2.NewTarget()
    t1.DeleteTarget()
    t2.DeleteTarget()
    bullet = 0
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls != []:
        delete = []
        t1.Move()
        t2.Move()
        if t1.live != 0:
            t1.DrawTarget()
        if t2.live != 0:
            t2.DrawTarget()
        for i in range(len(balls)):
            balls[i].Move()
            if balls[i].hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if balls[i].hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', "")
                canv.bind('<ButtonRelease-1>', "")
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.itemconfig(t1.GetIDPoints(), text=t1.GetScore())
            balls[i].draw_ball()
            if balls[i].ball_stop() == True:
                balls[i].delete_ball()
                delete.append(i)
        for i in delete:
            del balls[i]

        canv.update()
        time.sleep(0.03)
        for b in balls:
            b.delete_ball()
        t1.DeleteTarget()
        t2.DeleteTarget()
        g1.targetting()
        g1.PowerUp()

    canv.delete(gun)
    canv.itemconfig(screen1, text='')


new_game()

while True:
    new_game()
