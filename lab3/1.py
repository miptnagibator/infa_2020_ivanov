import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 300))
black = (0, 0, 0)
white = (225, 225, 225)

rect(screen, (165, 220, 232), (0, 0, 500, 150))
rect(screen, (24, 138, 22), (0, 150, 500, 150))

rect(screen, (148, 89, 0), (60, 123, 140, 90))
rect(screen, (68, 171, 171), (110, 150, 40, 40))
rect(screen, black, (60, 123, 140, 90), 2)
polygon(screen, (255, 0, 0), [(130, 63), (60, 123), (200, 123), (130, 63)])
polygon(screen, black, [(130, 63), (60, 123), (200, 123), (130, 63)], 2)

circle(screen, white, (225, 55), 20)
circle(screen, black, (225, 55), 20, 1)
circle(screen, white, (245, 55), 20)
circle(screen, black, (245, 55), 20, 1)
circle(screen, white, (265, 55), 20)
circle(screen, black, (265, 55), 20, 1)
circle(screen, white, (285, 55), 20)
circle(screen, black, (285, 55), 20, 1)
circle(screen, white, (270, 40), 20)
circle(screen, black, (270, 40), 20, 1)
circle(screen, white, (245, 40), 20)
circle(screen, black, (245, 40), 20, 1)

rect(screen, black, (370, 140, 10, 60))
circle(screen, black, (358, 125), 22, 2)
circle(screen, black, (390, 128), 22, 2)
circle(screen, black, (370, 110), 22, 2)
circle(screen, black, (352, 96), 22, 2)
circle(screen, black, (397, 92), 22, 2)
circle(screen, black, (374, 75), 22, 2)
circle(screen, (39, 107, 58), (358, 125), 20)
circle(screen, (39, 107, 58), (390, 128), 20)
circle(screen, (39, 107, 58), (370, 110), 20)
circle(screen, (39, 107, 58), (352, 96), 20)
circle(screen, (39, 107, 58), (397, 92), 20)
circle(screen, (39, 107, 58), (374, 75), 20)

circle(screen, (255, 179, 216), (465, 50), 23)
circle(screen, black, (465, 50), 23, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()