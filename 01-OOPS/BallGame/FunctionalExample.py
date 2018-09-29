import pygame
import random

pygame.init()

width = 1000
height = 500

red = 255,0,0
white = 255,255,255

screen = pygame.display.set_mode((width, height))

def game(x,y):
    radius = 50
    moveX = 1
    moveY = 1
    print("Ball created...")
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        pygame.draw.circle(screen, red, [x, y], radius)

        x += moveX
        y += moveY

        if x > width - radius:
            moveX = -1
        elif x < 50:
            moveX = 1
        elif y > height - radius:
            moveY = -1
        elif y < 50:
            moveY = 1

        pygame.display.update()

game(50,50)
game(150,150)
game(250,250)