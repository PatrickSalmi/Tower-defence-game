import pygame
from gamelogic.tower_defence import TowerDefence
from gameloops.gameloop import Gameloop
from gameloops.renderer import Renderer
from gameloops.clock import Clock


def main():
    display = pygame.display.set_mode((960, 720))
    pygame.display.set_caption("Tower Defence")

    game = TowerDefence()
    renderer = Renderer(display, game)
    clock = Clock()
    game_loop = Gameloop(display, renderer, clock, game)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
