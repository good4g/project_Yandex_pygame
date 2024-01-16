import pygame
import random
from slider import Slider

from border import horizontal_borders, vertical_borders, all_sprites

sprites_c = pygame.sprite.Sprite()


class Circle(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        self.mask = pygame.mask.from_surface(self.image)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.sprite_circle = pygame.sprite.Sprite()
        self.sprite_circle.image = self.image
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)
        #self.s = Slider()

        #self.sprite_circle.rect = self.sprite_circle.image.get_rect().move(400, 200)
        #self.group_circle = pygame.sprite.Group()
        #self.group_circle.add(self.sprite_circle)

    def update(self):
        #s = Slider().group
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy *= -1
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx *= -1
        #if pygame.sprite.collide_mask(self, self.s):
            #self.rect.move(0, 1)
