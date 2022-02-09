import pygame
import sys
from settings import  *
from sheep import Ship


def run():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    sheep = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit
                quit()

        screen.fill(black)
        sheep.drawing()
        pygame.display.flip()  # Last Screen


run()