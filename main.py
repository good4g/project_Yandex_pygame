import pygame
from rectangle import Rectangle


def make_form(*args):
    for x in range(args[0], args[1], args[2]):
        for y in range(args[3], args[4], args[5]):
            figure = Rectangle('rect.jpg')
            print(figure.size_x_9)
            figure.update(x, y)
            figure.all_sprites_rectangle.draw(screen)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        make_form(200, 600, 38, 0, 140, 17)

        pygame.display.flip()
    pygame.quit()