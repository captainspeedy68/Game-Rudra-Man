import pygame
pygame.init()

# create game window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rudra Man")

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for drawing background


#game loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()