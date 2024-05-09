import pygame


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_img(self, frame_w, frame_h, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame_w * width),
                (frame_h * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet

        h = self.demon_height
        w = self.size
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(
                    # x * self.size, y * self.size, self.size, self.size)
                    x * w, y * h, w, h)

                temp_img_list.append(pygame.transform.scale(
                    temp_img, ((w * self.image_scale), (h * self.image_scale))))
            animation_list.append(temp_img_list)
        # print(animation_list)
        return animation_list