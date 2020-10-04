import pygame
from pygame.draw import *

pygame.init()
width = 500 #Ширина граф. окна
height = 300 #Высота граф. окна


FPS = 30
screen = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (225, 225, 225)


def draw_sky_and_ground(width, height, dot):
    '''
    Функция рисует небо и землю на экране.
    :param width: Ширина экрана.
    :param height: Высота экрана.
    :param dot: Расстояние по y от 0 до линии разделения земли и неба.
    :return: None
    '''
    rect(screen, (165, 220, 232), (0, 0, width, dot)) #Рисует небо.
    rect(screen, (24, 138, 22), (0, dot, width, height-dot)) #Рисует землю.


def draw_house(x, y, width, height):
    '''
    Функция рисует дом. Весь дом вписан в прямоугольник,
    шириной width и высотой height,
    у которого левый верхний угол имеет координту (x,y).
    :param x: Координата по x левого верхнего угла дома.
    :param y: Координата по y левого верхнего угла дома.
    :param width: Ширина дома.
    :param height: Высота дома.
    :return: None
    '''
    rect(screen, (148, 89, 0), (x, y +height/3, width, 2*height/3))
    rect(screen, (68, 171, 171), (x + 0.36*width, y +height*0.3 + height/4, 0.3*width, 0.27*height))
    rect(screen, black, (x, y +height/3, width, 2*height/3), 2)
    polygon(screen, (255, 0, 0), [[x, y+height*(1/3) ], [x+ width/2, y], [x+width, y+ (1/3)*height]])
    polygon(screen, black, [[x, y + height * (1 / 3)], [x + width / 2, y], [x + width, y + (1 / 3) * height]],2)


def draw_cloud(x,y, radius):
    '''
    Функция рисует облако из 6 кругов радиуса radius,
    которые вписаны в прямоугольник ширины 5*radius и высоты (7/4)*radius,
    у которго координата верхнего левого угла имеет значение (x,y).
    :param x: Координата по x левого верхнего угла прямоугольник.
    :param y: Координата по y левого верхнего угла прямоугольник.
    :param radius: Радиус окружности.
    :return: None
    '''
    circle(screen, white, (x+radius, int(y+radius+radius*(3/4))), radius)
    circle(screen, black, (x + radius, int(y + radius + radius * (3 / 4))), radius,1)

    circle(screen, white, (x+2*radius, int(y+radius+radius*(3/4))), radius)
    circle(screen, black, (x + 2 * radius, int(y + radius + radius * (3 / 4))), radius,1)

    circle(screen, white, (x+3*radius, int(y+radius+radius*(3/4))), radius)
    circle(screen, black, (x + 3 * radius, int(y + radius + radius * (3 / 4))), radius,1)

    circle(screen, white, (x+4*radius, int(y+radius+radius*(3/4))), radius)
    circle(screen, black, (x + 4 * radius, int(y + radius + radius * (3 / 4))), radius,1)

    circle(screen, white, (x + int(radius*(13/4)) , y+radius), radius)
    circle(screen, black, (x + int(radius * (13 / 4)), y + radius), radius,1)

    circle(screen, white, (x+radius*2, y+radius), radius)
    circle(screen, black, (x + radius * 2, y + radius), radius,1)


def draw_tree(x,y,width,height):
    '''
    Функция рисует дерево из прямоуголька и кругов,
    которое вписано в прямоугольник ширины width и высоты height,
    у которго координата верхнего левого угла имеет значение (x,y).
    :param x: Координата по x левого верхнего угла прямоугольник.
    :param y: Координата по y левого верхнего угла прямоугольник.
    :param width: Ширина прямоугольника.
    :param height: Высота прямоугольника.
    :return: None
    '''
    scr = pygame.Surface([89,147], pygame.SRCALPHA)
    rect(scr, black, (370-332, 140-55, 10, 60))
    circle(scr, black, (358-330, 125-52), 22,2)
    circle(scr, black, (390-330, 128-52), 22,2)
    circle(scr, black, (370-330, 110-52), 22,2)
    circle(scr, black, (352-330, 96-52), 22,2)
    circle(scr, black, (397-330, 92-52), 22,2)
    circle(scr, black, (374-330, 75-52), 22,2)

    circle(scr, (39, 107, 58), (358-330, 125-52), 20)
    circle(scr, (39, 107, 58), (390-330, 128-52), 20)
    circle(scr, (39, 107, 58), (370-330, 110-52), 20)
    circle(scr, (39, 107, 58), (352-330, 96-52), 20)
    circle(scr, (39, 107, 58), (397-330, 92-52), 20)
    circle(scr, (39, 107, 58), (374-330, 75-52), 20)

    pygame.transform.scale(scr,(width-2,height-2) )
    screen.blit(scr, [x, y])


def draw_sun(x,y,radius):
    '''
    Функция рисует солнце, цент которго находится в (x,y),
    радиус которого = radius
    :param x: Координата по x центра круга.
    :param y: Координата по y центра круга.
    :param radius: Радиус солнца.
    :return: None
    '''
    circle(screen, (255, 179, 216), (x, y), radius)
    circle(screen, black, (x, y), radius, 1)


draw_sky_and_ground(width,height,150)
draw_house(60,63,140,150)
draw_cloud(205, 20 ,20)
draw_tree(338,55, 89,147 )
draw_sun(465,50,23)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()