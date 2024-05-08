import pygame
from fighter import Fighter
pygame.init()

# create game window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rudra Man")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#load spreadshits
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))
    
#function for drawing health bars
def draw_health_bar(health, x, y):
    ratio  = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    
    
#create 2 instances of fighter
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
run = True

while run:
    clock.tick(FPS)
    #draw backgroun
    draw_bg()
    
    #show player stats
    draw_health_bar(fighter_2.health, 20, 20)
    draw_health_bar(fighter_1.health, 580, 20)
    
    #move fighters
    fighter_1.move(screen_width, screen_height, screen, fighter_2)
    # fighter_2.move()
    
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()