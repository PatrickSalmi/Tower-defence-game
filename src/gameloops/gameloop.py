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

            self.game.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if self.game.health <= 0:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.game.ingame_menu.buy_tower.rect.collidepoint(pos):
                    if not self.game.ingame_menu.tower_selected:
                        self.game.ingame_menu.tower_selected = True
                elif self.game.ingame_menu.tower_selected:
                    self.game.place_tower(pos)
                    self.game.ingame_menu.tower_selected = False
            

    def render(self):
        self.renderer.render()
