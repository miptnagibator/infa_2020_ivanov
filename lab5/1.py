import pygame
from pygame.draw import *
import random

# let's declare our colors
house_col = (62, 38, 36)
roof_column_col = (10, 10, 10)
terrace_col = (115, 81, 77)
wind_on_moon_col = (220, 218, 186)
wind_off_col = (0, 0, 0)
clouds_col = (80, 79, 61, 100)
new_clouds_col = (186, 176, 167, 100)
ghost_col = (208, 207, 204, 10)
pipe_col = (69, 69, 69)
sky_col = (156, 149, 120)
moon_col = (220, 218, 186)
# colours declared!

# set canvas size
width = 600
height = 600
canvasDims=[width,height]
# in case it can be easily changed

# then use it
screen = pygame.display.set_mode(canvasDims)
surface = pygame.display.set_mode(canvasDims, pygame.SRCALPHA)
screen.blit(surface, (0, 0))
FPS = 30
pygame.init()


def foundation(x, y, sc, w, h):  # this function draws the foundation of the houses
    rect(sc, house_col, (x, y, w, h))
    polygon(sc, roof_column_col,
            [(x - w / 15, y), (x + w / 15, y - h / 15), (x + 14 * w / 15, y - h / 15), (x + 16 * w / 15, y)])


def pipes(x, y, sc, w, h):  # draws pipes
    n = random.randint(0, (7 * w // 150) + 2)
    for i in range(n):
        hp = random.randint(20 * h // 300, 30 * h // 300)
        wp = random.randint(10 * w // 150, 15 * w // 150)
        rect(sc, pipe_col, (x + w / 10 + (w * 4 / 5) / n * i, y - h / 15 - hp, wp, hp))


def terrace(x, y, sc, w, h):  # draw balcony/terrace or whatever that is
    col_w = w / 11
    for i in range(6):
        rect(sc, roof_column_col, (x + 2 * col_w * i, y, col_w, h / 2))
    rect(sc, terrace_col, (x - w / 15, y + h * 2 / 5, w * 17 / 15, 10))
    for i in range(5):
        rect(sc, terrace_col, (x + col_w + 2 * col_w * i, y + h * 2 / 5 + h / 30, col_w, h / 10))
    rect(sc, terrace_col, (x - 10, y + h / 2, w + 20, 20))


def windows(x, y, sc, w, h):  # draws windows
    wind_size = w / 3 - w / 7.5
    for i in range(3):
        if random.randint(0, 10) > 6:
            rect(sc, wind_on_moon_col, (x + w / 15 + (w / 7.5 + wind_size) * i, y + 3 * h / 4, wind_size, wind_size))
        else:
            rect(sc, wind_off_col, (x + w / 15 + (w / 7.5 + wind_size) * i, y + 3 * h / 4, wind_size, wind_size))


def house(x, y, sc, w, h):  # draws complete house
    foundation(x, y, sc, w, h)
    pipes(x, y, sc, w, h)
    terrace(x, y, sc, w, h)
    windows(x, y, sc, w, h)


def cloud_maker(sc, ymin, ymax, x, color):  # draws clouds
    num = random.randint(3, 5)
    for i in range(num):
        x1 = random.randint(0, x)
        y1 = random.randint(ymin, ymax // 2)
        w = random.randint(x // 3, x // 2)
        h = random.randint(ymin // 10, w // 5)
        ellipse(sc, color, (x1, y1, 2 * w, h))


def ghost_buddy(sc, x_center, y_center, size=1):  # draws a ghost
    r = 30 * size
    ellipse(sc, ghost_col, (x_center - r, y_center - r, 2 * r, 2 * r))
    for i in range(6):
        ellipse(sc, ghost_col, (x_center - 1.2 * r + 10 * i * size, y_center, 21 * size, 2.5 * r))
    ellipse(sc, wind_off_col, (x_center - r / 3 - 5 * size, y_center - r / 2, 10 * size, 20 * size))
    ellipse(sc, wind_off_col, (x_center + r / 3 - 5 * size, y_center - r / 2, 10 * size, 20 * size))
    ellipse(sc, wind_off_col, (x_center - 7 * size, y_center + r / 4, 14 * size, r))


rect(screen, sky_col, (0, 0, 600, 300))  # sky
ellipse(screen, moon_col, (200, 20, 80, 80))  # moon

cloud_maker(surface, 0, 150, 600, clouds_col)        #
house(10, 150, screen, 150, 300)                     #
house(300, 200, screen, 75, 150)                     #
house(400, 100, screen, 200, 400)                    #
cloud_maker(surface, 0, 150, 600, new_clouds_col)    # basically this is where our programme does what it should do
ghost_buddy(surface, 200, 400)                       #
ghost_buddy(surface, 250, 300, 0.5)                  #
ghost_buddy(surface, 400, 400, 2)                    #
cloud_maker(surface, 200, 600, 600, new_clouds_col)  #

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()