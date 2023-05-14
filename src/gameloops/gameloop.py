import pygame
from ui.main_menu import MainMenu
from ui.score_board import ScoreBoard


class Gameloop:
    def __init__(self, display, renderer, clock, game):
        self.display = display
        self.renderer = renderer
        self.clock = clock
        self.game = game
        self.main_menu = MainMenu()
        self.score_board = ScoreBoard()
        self.quit = False

    def start(self):
        while True:
            if self.handle_menu_events() == False:
                break

            self.main_menu.draw_all(self.display)
            pygame.display.update()

    def handle_menu_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.main_menu.play_button.rect.collidepoint(pos):
                    self.play()
                if self.main_menu.scores_button.rect.collidepoint(pos):
                    self.score_board.load_scores()
                    self.scores()

    def scores(self):
        while True:
            if self.handle_scores_events() == False:
                break

            self.score_board.draw_all(self.display)
            pygame.display.update()

    def handle_scores_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.score_board.back_button.rect.collidepoint(pos):
                    return False

    def play(self):
        while True:
            if self.handle_game_events() == False:
                break

            self.game.update()
            self.render()
            self.clock.tick(60)

    def handle_game_events(self):
        pos = pygame.mouse.get_pos()
        ig_menu = self.game.ingame_menu
        score_screen = self.game.score_screen
        ig_menu.set_tower_preview(pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tower_clicked = False

                    if ig_menu.retire_button.rect.collidepoint(pos) and not self.game.game_over:
                        self.game.end_game()

                    if score_screen.back_button.rect.collidepoint(pos):
                        self.game.reset_game()
                        return False

                    if ig_menu.pause_button.rect.collidepoint(pos) and not self.game.game_over:
                        self.game.toggle_pause()
                        ig_menu.sell_mode = False

                    if not self.game.pause:

                        for tower in self.game.towers:
                            if tower.rect.collidepoint(pos):
                                tower.clicked = not tower.clicked
                                tower_clicked = True

                        if not tower_clicked:
                            for tower in self.game.towers:
                                tower.clicked = False

                        if not ig_menu.sell_mode and ig_menu.basic_tower.rect.collidepoint(pos):
                            ig_menu.tower_type = None

                            if not ig_menu.tower_selected:
                                ig_menu.tower_selected = True

                        elif not ig_menu.sell_mode and ig_menu.sniper_tower.rect.collidepoint(pos):
                            ig_menu.tower_type = "sniper"

                            if not ig_menu.tower_selected:
                                ig_menu.tower_selected = True

                        elif ig_menu.tower_selected:
                            self.game.place_tower(pos, ig_menu.tower_type)
                            ig_menu.tower_selected = False
                            ig_menu.tower_preview = None

                        elif ig_menu.sell_button.rect.collidepoint(pos) and not ig_menu.tower_selected:
                            if not ig_menu.sell_mode:
                                ig_menu.sell_mode = True
                            else:
                                ig_menu.sell_mode = False

                        elif ig_menu.sell_mode:
                            for tower in self.game.towers:
                                if tower.rect.collidepoint(pos):
                                    self.game.sell_tower(tower)
                                    break

                        else:
                            ig_menu.sell_mode = False
                            ig_menu.tower_selected = False

                elif event.button == 3:
                    ig_menu.sell_mode = False
                    ig_menu.tower_selected = False
                    ig_menu.tower_preview = None
                    for tower in self.game.towers:
                        tower.clicked = False

    def render(self):
        self.renderer.render()
