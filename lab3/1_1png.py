import pygame
from pygame.draw import *
from math import pi
from math import sin, cos

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

rect(screen, (0, 191, 255), (0,0, 600*2,400*2)) #sky
rect(screen, (0, 0, 128), (0,150*2, 600*2,400*2)) #sea
rect(screen, (255, 222, 173), (0,250*2, 600*2,400*2)) #sand


def cloud(x, y, width, hight): #draw cloud
    #draw the 1st circle
    pygame.draw.ellipse(screen,(255,255,255) , (x, y, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x, y, width, hight),1)
    #draw the 2nd circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width*0.7, y + hight*0.07 , width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width*0.7, y + hight*0.07, width, hight), 1)
    #draw the 3rd circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width * 1.3, y + hight * 0.1, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width * 1.3, y + hight * 0.1, width, hight), 1)
    #draw the 4th circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width * 1.8, y + hight * 0.2, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width * 1.8, y + hight * 0.2, width, hight), 1)
    #draw the 5th circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width * 1.6, y - hight * 0.3, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width * 1.6, y - hight * 0.3, width, hight), 1)
    #draw the 6th circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width * 1.0, y - hight * 0.5, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width * 1.0, y - hight * 0.5, width, hight), 1)
    #draw the 7th circle
    pygame.draw.ellipse(screen, (255, 255, 255), (x + width * 0.4, y - hight * 0.4, width, hight))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + width * 0.4, y - hight * 0.4, width, hight), 1)


def ship(x, y, width, height):
    #draw the main part
    pygame.draw.rect(screen, (139, 69, 19), (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height),1)
    #draw the triangle
    pygame.draw.polygon(screen, (139, 69, 19), ([x + width, y], [x + width, y + height-1], [x + width + width*0.5, y]) )
    pygame.draw.polygon(screen, (0, 0, 0), ([x + width, y], [x + width, y + height-1], [x + width + width * 0.5, y]), 1)
    #draw the segment of a circle
    l = [[x,y]]
    n = 100
    alpha = 90
    dalpha = 90/n
    for i in range(n):
        xn = x + height*cos(2*pi*alpha/360)
        yn = y + height*sin(2*pi*alpha/360)
        alpha+=dalpha
        l.append([xn,yn])
    pygame.draw.polygon(screen,(139, 69, 19), l)
    pygame.draw.polygon(screen, (0,0,0), l, 1)
    #draw the eye
    pygame.draw.circle(screen, (0,0,0), (x + int(1.15*width) , y + int(0.35*height)), int(height*0.25))
    pygame.draw.circle(screen, (255, 255, 255), (x + int(1.15 * width), y + int(0.35 * height)), int(height * 0.15))
    #draw the stick
    pygame.draw.rect(screen, (0,0,0), (x + width/2, y - height*3 , width*0.03, height*3))
    #draw the sail
    pygame.draw.polygon(screen, (255, 250, 205), [[x + width/2 + width*0.03, y - height*3], [x + width/2 + width*0.35, y - height*1.5], [x + width/2 + width*0.1, y - height*1.5]])
    pygame.draw.polygon(screen, (255, 250, 205), [[x + width / 2 + width * 0.03, y], [x + width / 2 + width * 0.35, y - height * 1.5], [x + width / 2 + width * 0.1, y - height * 1.5]])
    pygame.draw.polygon(screen, (0, 0, 0), [[x + width / 2 + width * 0.03, y - height * 3], [x + width / 2 + width * 0.35, y - height * 1.5], [x + width / 2 + width * 0.1, y - height * 1.5]],1)
    pygame.draw.polygon(screen, (0, 0, 0), [[x + width / 2 + width * 0.03, y], [x + width / 2 + width * 0.35, y - height * 1.5], [x + width / 2 + width * 0.1, y - height * 1.5]], 1)


def umbrella(x, y, width, height):
    #draw stick
    pygame.draw.rect(screen, (160, 82, 45), (x, y, width, height))
    #draw triangle
    pygame.draw.polygon(screen, (255, 20, 147), [[x + width/2 - width*10, y + height/4], [x, y], [x+width, y], [x + 10.5*width, y + height/4] ])
    pygame.draw.polygon(screen, (0,0,0), [[x + width / 2 - width * 10, y + height / 4], [x, y], [x + width, y],[x + 10.5 * width, y + height / 4]], 1)
    pygame.draw.rect(screen, (0,0,0), (x, y, width, height),1)
    #draw lines
    for i in range(4):
        pygame.draw.line(screen, (0,0,0),[x,y], [x + width/2 - width*10 + i*10*width/4, y + height/4])
        pygame.draw.line(screen, (0, 0, 0), [x+width, y], [x + 10.5*width - i*10*width/4, y + height/4])


def waves(y,width,height): #draw the sand wawes
    l = [[0,800],[0,y]]
    for i in range(width):
        s = y + height*sin(0.04*i)
        l.append([i,s])
    l.append([width, 800])
    rect(screen, (0, 0, 128), (0, 150 * 2, 600 * 2, 400 * 2))
    pygame.draw.polygon(screen, (0,0,0), l,1)
    pygame.draw.polygon(screen, (255, 222, 173), l)


def sun (x,y,radius,ray): #draw sun with rays
    l = [[x, y]]
    n = 100
    alpha = 0
    dalpha = 360 / n
    for i in range(n+1):
        if i%2 ==0:
            xn = x + ray*radius * cos(2 * pi * alpha / 360)
            yn = y + ray*radius * sin(2 * pi * alpha / 360)
            alpha += dalpha
            l.append([xn, yn])
        else:
            xn = x + radius * cos(2 * pi * alpha / 360)
            yn = y + radius * sin(2 * pi * alpha / 360)
            alpha += dalpha
            l.append([xn, yn])
    pygame.draw.polygon(screen, (255, 255, 0), l)

#раскоментируйте, чтобы получить усложненную версию
waves(500,1200,15)
umbrella(420, 450, 7, 200)
cloud(180,170,80,100)
cloud(450,100,150,100)
ship(400,350,150,30)
sun(1000,100,75, 1.2)

ship(700,400, 300,60)
sun(1000,100,75, 1.0)
umbrella(150,360, 15, 350)
cloud(40,50,65,65)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()