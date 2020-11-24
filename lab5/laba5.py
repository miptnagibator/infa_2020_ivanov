import pygame
from pygame.draw import *

pygame.init()
import math
import pygame
from pygame.draw import *
from random import randint

pygame.init()

nickname = input("Nickname ")

time = 10  # время длительности игры в секундах
FPS = 60
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
image = pygame.image.load('countryball.png')

score = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

file = open("top.txt", 'a')


def new_ball():  # Функция создает новый шарик случайного радиуса, случайного цвета.
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    return [x, y, r, color, dx, dy]


def new_square():  # Функция создает новый квадрат случайного цвета со случайной стороной
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(60, 100)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x, y, a, a))
    dx = randint(-10, 10)
    dy = randint(-50, 50)
    dvx = 0
    dvy = randint(1, 5)
    return [x, y, a, color, dx, dy, dvx, dvy]


def click(event):  # Функция возвращает координаты щелчка мыши
    (x, y) = event.pos
    return [x, y]


def hit_ball(func_click, balls_pos):  # Функция проверяет, был ли клик внутри шара, если да, то прибавляет 1 очко
    global score
    for i in range(len(balls_pos)):
        if math.sqrt((func_click[0] - balls_pos[i][0]) ** 2 + (func_click[1] - balls_pos[i][1]) ** 2) <= balls_pos[i][
            2]:
            del balls_pos[i]
            balls_pos.append(new_ball())
            score += 1


def hit_square(func_click, square_pos):  # Функция проверяет, был ли клик внутри квадрата, если да, то прибавляет 3 очка
    global score
    for i in range(len(square_pos)):
        if 0 < (func_click[0] - square_pos[i][0]) < square_pos[i][0]:
            if 0 < (func_click[1] - square_pos[i][1]) < square_pos[i][0]:
                del square_pos[i]
                square_pos.append(new_square())
                score += 3


def score_show(score):  # Функция выводит количество очков
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Score: ' + str(score), 1, (180, 0, 0))
    screen.blit(text1, (10, 50))


balls_pos = []
square_pos = []

# Циклы добавляют параметры шаров и квадратов в массив.
for i in range(15):
    balls_pos.append(new_ball())
for i in range(5):
    square_pos.append(new_square())


def move_balls(balls_pos):  # Функция перемещает шары в соответствии с их параметрами из массива.
    for i in range(len(balls_pos)):
        balls_pos[i][0] += balls_pos[i][4]
        balls_pos[i][1] += balls_pos[i][5]

        if balls_pos[i][0] + balls_pos[i][2] >= screen_width:
            balls_pos[i][0] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        if balls_pos[i][0] - balls_pos[i][2] <= 0:
            balls_pos[i][0] -= balls_pos[i][4]
            balls_pos[i][4] = - balls_pos[i][4]

        if balls_pos[i][1] + balls_pos[i][2] >= screen_height:
            balls_pos[i][1] -= balls_pos[i][5]
            balls_pos[i][5] = - balls_pos[i][5]

        if balls_pos[i][1] - balls_pos[i][2] <= 0:
            balls_pos[i][1] -= balls_pos[i][5]
            balls_pos[i][5] = - balls_pos[i][5]

        circle(screen, balls_pos[i][3], (balls_pos[i][0], balls_pos[i][1]), balls_pos[i][2])


def move_squares(square_pos, image):  # Функция перемещает квадраты в соответствии с их параметрами из массива.
    for i in range(len(square_pos)):
        square_pos[i][0] += square_pos[i][4]
        square_pos[i][1] += square_pos[i][5]
        square_pos[i][4] += square_pos[i][6]
        square_pos[i][5] += square_pos[i][7]

        if square_pos[i][0] + square_pos[i][2] >= screen_width:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        if square_pos[i][0] <= 0:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        if square_pos[i][1] + square_pos[i][2] >= screen_height:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] -= square_pos[i][5] * 0.2 - 0.01

        if square_pos[i][1] <= 0:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] += square_pos[i][5] * 0.2 - 0.01

        rect(screen, square_pos[i][3], (square_pos[i][0], square_pos[i][1], square_pos[i][2], square_pos[i][2]))
        scr = pygame.Surface([square_pos[i][2], square_pos[i][2]], pygame.SRCALPHA)
        scr.blit(image, (0, 0))

        screen.blit(scr, (square_pos[i][0], square_pos[i][1]))
        new_image = pygame.transform.scale(image, (square_pos[i][2], square_pos[i][2]))
        screen.blit(new_image, (square_pos[i][0], square_pos[i][1]))


pygame.display.update()
clock = pygame.time.Clock()
finished = 0

while finished < time * FPS:
    clock.tick(FPS)
    print(balls_pos)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit_ball(click(event), balls_pos)
            hit_square(click(event), square_pos)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    score_show(score)
    move_balls(balls_pos)
    move_squares(square_pos, image)
    pygame.display.update()
    screen.fill(BLACK)
    finished += 1

file.write(nickname + " " + str(score) + '\n')
file.close()
pygame.quit()

file = open('top.txt', 'r')
data = []

while True:
    a = file.readline()
    if a == "":
        break
    data.append(a)
for i in range(len(data)):
    a = data[i]
    a = a.split()
    data[i] = a

print(data)
file.close()


def sort_col(i):
    return int(i[1])


data.sort(key=sort_col)
print(data)
file.close()

file = open('top.txt', 'w')
for i in range(len(data)):
    file.write(str(data[i][0]) + " " + str(data[i][1]) + "\n")
