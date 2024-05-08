import pygame
from fighter import Fighter
pygame.init()

# create game window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rudra Man")

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))
    
#create 2 instances of fighter
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(200, 310)

#game loop
run = True

while run:
    #draw backgroun
    draw_bg()
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()