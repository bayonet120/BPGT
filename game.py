import pygame

def Main():
    # Variables
    x = 615
    y = 335

    # Initializing pygame
    pygame.init()

    # Creating the window
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Bayonet's Pygame Thing")

    # Colors
    RED = (255,0,0)

    # Game loop
    running = True
    while running: 	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            screen.fill((0,255,0)) 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y -= 20
                if event.key == pygame.K_s:
                    y += 20
                if event.key == pygame.K_a:
                    x -= 20
                if event.key == pygame.K_d:
                    x += 20

        square01 = pygame.draw.rect(screen, RED, (x,y,50,50))
        pygame.display.update()

Main()
