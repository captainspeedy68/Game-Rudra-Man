import pygame
from fighter import Fighter
from pygame import mixer
mixer.init()
pygame.init()

# create game window
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rudra Man")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE= 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
DEMON_HEIGHT = 160
DEMON_WIDTH = 288
DEMON_SCALE = 3
DEMON_OFFSET = [112, 107]
DEMON_DATA = [DEMON_HEIGHT, DEMON_WIDTH, DEMON_SCALE, DEMON_OFFSET]


#load images and sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.4)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.6)

# load bg image
bg_image = pygame.image.load(
    "assets/images/background/background.jpg").convert_alpha()

# load spreadshits
warrior_sheet = pygame.image.load(
    "assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load(
    "assets/images/wizard/Sprites/wizard.png").convert_alpha()
demon_sheet = pygame.image.load(
    "assets/images/boss_demon_slime_FREE_v1.0/spritesheets/demon.png").convert_alpha()

#load victory image
victory_img =pygame.image.load("assets/images/icons/victory.png").convert_alpha()

# define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
DEMON_ANIMATION_STEPS = [5, 11, 14, 4, 22]

#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

#define function for drawing text

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))

# function for drawing health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create 2 instances of fighter
fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, False)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, False)
# fighter_3 = Fighter(2, 500, 310, True, WIZARD_DATA, demon_sheet, DEMON_ANIMATION_STEPS, magic_fx, True)
# fighter_2 = Fighter(2, 700, 310, True, DEMON_DATA, demon_sheet, DEMON_ANIMATION_STEPS)

# game loop
run = True

while run:
    clock.tick(FPS)
    # draw backgroun
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
    
    if intro_count <= 0:
        # move fighters
        fighter_1.move(screen_width, screen_height, screen, fighter_2, round_over)
        fighter_2.move(screen_width, screen_height, screen, fighter_1, round_over)
    else:
        #display count timer
        draw_text(str(intro_count), count_font, RED, screen_width / 2, screen_height / 3)
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
            print(intro_count)


    #update fighters
    fighter_1.update()
    fighter_2.update()
    # fighter_3.update()
    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    # fighter_3.draw(screen)

    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
            print(score)
    else:
        #display victory image
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx, False)
            fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx, False)
            # fighter_3 = Fighter(2, 500, 310, True, WIZARD_DATA, demon_sheet, DEMON_ANIMATION_STEPS, magic_fx)
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
