import pygame
import os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data_ph', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, name_photo):
        super().__init__()
        self.size = load_image(name_photo).get_size()
        self.size_x_9 = (self.size[0] / (max(self.size) / min(self.size) * 9),
                         self.size[1] / (max(self.size) / min(self.size) * 9))
        self.image = pygame.transform.scale(load_image(name_photo, -1),
                                            (int(self.size_x_9[0]), int(self.size_x_9[1])))
        self.all_sprites_rectangle = pygame.sprite.Group()
        self.sprite_rect = pygame.sprite.Sprite()
        self.all_sprites_rectangle.add(self.sprite_rect)

    def update(self, x, y):
        self.sprite_rect.image = self.image
        self.sprite_rect.rect = self.sprite_rect.image.get_rect().move(x, y)

