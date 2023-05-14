import pygame
from pygame.sprite import Group
from gamelogic.wave_logic import Waves
from sprites.towers import Tower
from ui.ingame_menu import IngameMenu
from ui.score_screen import ScoreScreen
from scores import save_scores


class TowerDefence():
    """Class for the game logic

    """

    def __init__(self):
        self.route = [(50, 0), (50, 200), (400, 200),
                      (400, 400), (800, 400), (800, 720)]

        self.pause = False

        self.route_rect = []
        self.create_route_rect()
        self.game_width = 960
        self.game_height = 720

        self.ingame_menu = IngameMenu()
        self.score_screen = ScoreScreen()

        self.score = 0
        self.health = 5
        self.money = 100
        self.game_over = False

        self.waves = Waves()

        self.towers = Group()
        self.all_sprites = Group()

    def valid_tower(self, tower):
        """ Checks if a tower is being placed on the route or on another tower

        Args:
            tower_rect: The tower objects shape

        Returns:
            bool: Returns False if Tower object rect collides with route line, otherwise True
        """

        for line in self.route_rect:
            if line.colliderect(tower.rect):
                return False

        for tower2 in self.towers:
            if tower.rect.colliderect(tower2.rect):
                return False

        return True

    def place_tower(self, pos, tower_type=None):
        """Adds a tower using the x and y values

        Args:
            x : x coordinate of the tower
            y : y coordinate of the tower
        """

        tower = Tower(pos, tower_type)
        if pos[0] < self.game_width - (tower.rect.width//2) and pos[1] < self.game_height - (tower.rect.height//2) and self.purchase_tower(tower):
            self.towers.add(tower)
            self.all_sprites.add(tower)

    def purchase_tower(self, tower):
        if self.money >= tower.price and self.valid_tower(tower):
            self.money -= tower.price
            return True

        return False

    def sell_tower(self, tower):
        self.money += tower.price // 2
        self.towers.remove(tower)
        self.all_sprites.remove(tower)

    def assign_targets(self, tower):
        """Assigns a enemy as a target for a tower

        Args:
            tower: tower object
        """
        for enemy in self.waves.enemies:
            if tower.target is None:
                tower.calculate_distance(enemy)
            else:
                break

    def create_route_rect(self):
        path_width = 20

        for i in range(len(self.route) - 1):
            start = self.route[i]
            end = self.route[i+1]

            if start[0] == end[0]:
                x = start[0] - path_width / 2
                y = start[1]
                width = path_width
                height = abs(start[1] - end[1])

            elif start[1] == end[1]:
                x = start[0]
                y = start[1] - path_width / 2
                width = abs(start[0] - end[0])
                height = path_width

            line_rect = pygame.Rect(x, y, width, height)
            self.route_rect.append(line_rect)

    def draw_all(self, display):
        display.fill((0, 128, 0))
        pygame.draw.lines(display, (128, 128, 128), False, self.route, 20)
        pygame.draw.line(display, (0, 0, 0), (960, 0), (960, 720), 3)

        self.all_sprites.draw(display)
        
        for tower in self.towers:
            if tower.clicked:
                tower.draw_range(display)

        if self.game_over:
            self.score_screen.draw_all(display)

        self.ingame_menu.draw_all(
            display, self.health, self.money, self.waves.wave_nro, self.waves.total_waves)

    def toggle_pause(self):
        self.pause = not self.pause
        self.ingame_menu.pause_button.alt = not self.ingame_menu.pause_button.alt

    def update(self):
        if self.pause:
            return

        self.waves.update(self.route, self.all_sprites)

        for enemy in self.waves.enemies:
            enemy.check_damage(pygame.time.get_ticks())
            if enemy.health <= 0:
                self.waves.enemies.remove(enemy)
                self.all_sprites.remove(enemy)
                self.money += 1
                
            if enemy.reached_end(self.route):
                self.health -= 1
                self.waves.enemies.remove(enemy)
                self.all_sprites.remove(enemy)

        for tower in self.towers:
            if tower.target is None:
                self.assign_targets(tower)

            if tower.attack(pygame.time.get_ticks()):
                tower.target.health -= tower.damage
                tower.target.take_damage(pygame.time.get_ticks())
        
        if self.health <= 0:
            self.end_game()

        if self.waves.wave_nro == self.waves.total_waves and not self.waves.enemies and self.waves.total_enemy_count == sum(self.waves.wave_enemy_spawns[self.waves.total_waves]):
            self.end_game()

    def calculate_score(self):
        self.score += (self.waves.wave_nro * 20)
        self.score += (self.health * self.waves.wave_nro * 5)
        self.score += (self.money * 2)

    def end_game(self):
        self.game_over = True
        self.pause = True
        self.calculate_score()
        save_scores(self.score)
        self.score_screen.get_score(
            self.waves.wave_nro, self.health, self.money, self.score)
        
    def reset_game(self):
        self.route = [(50, 0), (50, 200), (400, 200),
                      (400, 400), (800, 400), (800, 720)]
        self.pause = False
        self.ingame_menu.pause_button.alt = False

        self.create_route_rect()

        self.score = 0
        self.health = 5
        self.money = 20
        self.game_over = False

        self.waves = Waves()
        self.waves.enemies.empty()
        self.towers.empty()
        self.all_sprites.empty()
