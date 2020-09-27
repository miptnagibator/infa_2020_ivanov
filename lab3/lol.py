import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255,255,255), (0,0, 400,400))

circle(screen, (255, 255, 0), (200,200), 120, 0)
circle(screen, (0, 0, 0), (200,200), 120, 2)

rect(screen, (0,0,0), (130,250, 140,25))

circle(screen, (255, 0, 0), (170,170), 30, 0)
circle(screen, (0, 0, 0), (170,170), 30, 1)
circle(screen, (0, 0, 0), (170,170), 15, )

circle(screen, (255, 0, 0), (250,170), 20, 0)
circle(screen, (0, 0, 0), (250,170), 20, 1)
circle(screen, (0, 0, 0), (250,170), 10, )

polygon(screen, (0,0,0), [  (200,120),(140, 150),(100,140),(150,120)])
polygon(screen, (0,0,0), [  (300,120),(240, 150),(200,150),(250,120)])

def DrawArc(surface, color, center, radius, startAngle, stopAngle, width=1):
    width -= 2
    for i in range(-2, 3):
        # (2pi rad) / (360 deg)
        deg2Rad = 0.01745329251
        rect = pygame.Rect(
            center[0] - radius + i,
            center[1] - radius,
            radius * 2,
            radius * 2
        )

        pygame.draw.arc(
            surface,
            color,
            rect,
            startAngle * deg2Rad,
            stopAngle * deg2Rad,
            width
        )




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()