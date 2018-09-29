import pygame
import random

pygame.init()

width = 1000
height = 500

red = 255,0,0
white = 255,255,255

screen = pygame.display.set_mode((width, height))

class Ball():

    def __init__(self):
        self.radius = 50
        self.x = random.randint(0,width - self.radius)
        self.y = random.randint(0,height - self.radius)
        self.moveX = 1
        self.moveY = 1

    def moveBall(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.radius:
            self.moveX = -1
        elif self.x < self.radius:
            self.moveX = 1
        elif self.y > height - self.radius:
            self.moveY = -1
        elif self.y < self.radius:
            self.moveY = 1

# ball_1 = Ball()
# ball_2 = Ball()

n = int(input("Enter number of balls : "))
balls = []
for i in range(n):
    ball = Ball()
    balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)

    # pygame.draw.circle(screen, red, [ball_1.x, ball_1.y], ball_1.radius)
    # ball_1.moveBall()
    #
    # pygame.draw.circle(screen, red, [ball_2.x, ball_2.y], ball_2.radius)
    # ball_2.moveBall()

    for i in range(len(balls)):
        pygame.draw.circle(screen, red, [balls[i].x, balls[i].y], balls[i].radius)
        balls[i].moveBall()

    ball_1 = balls[0]
    ball_2 = balls[1]

    dist_x = abs(ball_1.x - ball_2.x)
    dist_y = abs(ball_1.y - ball_2.y)

    if dist_x <= 40 or dist_y <= 40:
        # print("Collision")
        ball_1.moveX *= -1
        ball_1.moveY *= -1
        ball_2.moveX *= -1
        ball_2.moveY *= -1

    pygame.display.update()
