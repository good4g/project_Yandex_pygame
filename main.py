import pygame
from rectangle import Rectangle
from slider import Slider
from circle import Circle
from border import Border
from border import all_sprites


def make_form(*args):
    figure = Rectangle('rect.png', 9)
    for x in range(args[0], args[1], args[2]):
        for y in range(args[3], args[4], args[5]):
            figure.update(x, y)
            figure.all_sprites_rectangle.draw(screen)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    s = Slider()
    c = Circle(10, 100, 200)
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                s.update(event.pos[0])
                #c.update()
        make_form(200, 600, 38, 0, 140, 17)
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(200)
        s.group.draw(screen)
        pygame.display.flip()
    pygame.quit()