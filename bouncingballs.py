import pygame
import sys
import random

random.seed(201)

screen_width = 720
screen_height = 360
background_color = (125,125,125)

screen = pygame.display.set_mode((screen_width,screen_height))

ball_image = pygame.image.load("ball.gif")
ball_rect = ball_image.get_rect()

pos = [random.random()*screen_width*0.5,random.random()*screen_height*0.5]
scale = random.randrange(-30,30)
ball_rect = ball_rect.inflate(scale,scale)
ball_rect = pygame.Rect(pos[0],pos[1],ball_rect.width,ball_rect.height)
ball_image = pygame.transform.scale(ball_image,(ball_rect.width,ball_rect.height))

direction = [1,1]

total_time_after_move = 0
inter_move_time = 10

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                inter_move_time += 1
            if event.key == pygame.K_UP:
                inter_move_time -= 1

    total_time_after_move += clock.get_time()
    if total_time_after_move < inter_move_time:
        clock.tick()
        continue

    total_time_after_move = 0

    ball_rect = ball_rect.move(direction)
    if (ball_rect.left <= 0) or (ball_rect.right >= screen_width):
        direction[0] = -direction[0]
    if (ball_rect.top <= 0) or (ball_rect.bottom >= screen_height):
        direction[1] = -direction[1]

    screen.fill(background_color)
    screen.blit(ball_image,ball_rect)
    pygame.display.flip()
    
    clock.tick()