import pygame


class Gameloop:
    def __init__(self, display, renderer, clock, game):
        self.display = display
        self.renderer = renderer
        self. clock = clock
        self.game = game

    def start(self):
        while True:
            if self.handle_events() == False:
                break

            self.game.spawn_enemies()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.game.spawn_enemies()
            
    def render(self):
        self.renderer.render()
