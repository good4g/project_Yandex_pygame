import pygame
from slider import Slider
from rectangle import load_image, Rectangle
from border import horizontal_borders, vertical_borders, all_sprites

pygame.init()
pygame.display.set_mode((800, 400))


class Circle(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image('circle3.png', -1), (35, 35))

        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.check = []
        self.vx = 2
        self.vy = 2
        self.s = Slider()

    def make_form(self, screen, *args):

        for x in range(args[0], args[1], args[2]):
            for y in range(args[3], args[4], args[5]):
                self.figure = Rectangle('rect.png', 9)
                self.figure.update(x, y)
                self.check += [self.figure]
                self.figure.all_sprites_rectangle.draw(screen)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy *= -1
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx *= -1
        if pygame.sprite.spritecollideany(self, self.s.group):
            self.vy *= -1

        for x in self.check:
            if pygame.sprite.spritecollideany(self, x.all_sprites_rectangle):
                self.vx *= -1
                self.vy *= -1
        self.check = []

