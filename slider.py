import pygame
from rectangle import load_image


class Slider(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(load_image('slider2.png'), (200, 40))
        self.rect, self.image = self.image.get_rect(), self.image
        self.group = pygame.sprite.Group()
        self.sprite_slider = pygame.sprite.Sprite()
        self.sprite_slider.image = self.image
        self.sprite_slider.rect, self.group.rect, self.group.image = self.image.get_rect(), self.image.get_rect(), self.image
        self.group.add(self.sprite_slider)

    def update(self, x):
        self.sprite_slider.rect = self.image.get_rect().move(x, 300)
