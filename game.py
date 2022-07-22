import pygame
from pygame.locals import *

def Main():
    # Variables
    vel_x = 10
    vel_y = 15
    jump = False
    dino = pygame.image.load('dino.png')
    dino_rect = dino.get_rect()
    obstacle01 = pygame.Rect(815,535,50,50)
    initial_dino_x = 615
    initial_dino_y = 535

    # Initializing pygame
    pygame.init()

    # Creating the window
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Bayonet's Pygame Thing")

    # Colors
    RED = (255,0,0)
    BLACK = (0,0,0)
    GREEN = (0,255,0)

    dino_rect.x = initial_dino_x
    dino_rect.y = initial_dino_y

    # Game loop
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT] and dino_rect.x > 0:
            dino_rect.x -= vel_x
        if userInput[pygame.K_RIGHT] and dino_rect.x < 1280:
            dino_rect.x += vel_x
        if jump is False and userInput[pygame.K_SPACE]:
            jump = True

        if jump is True:
            dino_rect.y -= vel_y
            vel_y -= 1
            if vel_y < -15:
                jump = False
                vel_y = 15

        if dino_rect.colliderect(obstacle01):
            if abs(obstacle01.top - dino_rect.bottom) < 20:
                dino_rect.bottom = obstacle01.top
            if abs(obstacle01.bottom - dino_rect.top) < 20:
                dino_rect.top = obstacle01.bottom
            if abs(obstacle01.right - dino_rect.left) < 11:
                dino_rect.left = obstacle01.right
            if abs(obstacle01.left - dino_rect.right) < 11:
                dino_rect.right = obstacle01.left

        if dino_rect.bottom != obstacle01.top and jump is False:
            print('you fall')
            dino_rect.y = initial_dino_y
            print(jump)

        screen.blit(dino, dino_rect)
        pygame.draw.rect(screen, RED, obstacle01, 4)

        pygame.time.delay(15)
        pygame.display.update()

Main()
#hey
