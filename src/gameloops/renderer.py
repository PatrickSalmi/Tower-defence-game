import pygame


class Renderer:
    def __init__(self, display, game):
        self.display = display
        self.game = game

    def render(self):
        self.game.draw_all(self.display)

        pygame.display.update()
