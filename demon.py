import pygame
import spritesheet
pygame.init()
# create game window
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Demon")


# load image
demon_sheet_image = pygame.image.load(
    "assets/images/boss_demon_slime_FREE_v1.0/spritesheets/demon.png").convert_alpha()

demon_sheet = spritesheet.SpriteSheet(demon_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

# timers
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame_x = 0
frame_y = 2
step_counter = 0

# create animation list
animation_list = []


# animation steps
DEMON_ANIMATION_STEPS = [6, 11, 14, 5, 22]
action = 2


for y, animation in enumerate(DEMON_ANIMATION_STEPS):
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(demon_sheet.get_img(step_counter, y, 288, 160, 2, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)
# print(animation_list)

run = True
while run:
    # update background
    screen.fill(BG)

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame_x += 1
        last_update = current_time
        if frame_x >= len(animation_list):
            frame_x = 0

        # screen.blit(animation_list[frame], (x * 288 * 2, 3))
    screen.blit(animation_list[action][frame_x], (frame_x , 3))
    # display image
    # screen.blit(demon_sheet, (0, 0))
    # show frame image
    # screen.blit(frame_0, (0, 0))
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
