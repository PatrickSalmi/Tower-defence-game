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
            
            if self.game.health <= 0:
                return False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] >= 0 and event.pos[0] <= 960 and event.pos[1] >= 0 and event.pos[1] <= 720:
                    self.game.add_tower(event.pos[0], event.pos[1])


    def render(self):
        self.renderer.render()
