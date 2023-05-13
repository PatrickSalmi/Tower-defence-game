import pygame
from pygame.sprite import Group
from sprites.enemies import Enemies
from sprites.towers import Tower
from ui.ingame_menu import IngameMenu


class TowerDefence():
    """Class for the game logic

    """

    def __init__(self):
        self.route = [(50, 0), (50, 200), (400, 200),
                      (400, 400), (800, 400), (800, 720)]

        self.route_rect = []
        self.create_route_rect()
        self.game_width = 960
        self.game_height = 720
        
        self.ingame_menu = IngameMenu()

        self.wave_nro = 1
        self.health = 5

        self.enemy_count = 0
        self.enemy_spawn_interval = 1000
        self.last_enemy_spawn = pygame.time.get_ticks()

        self.enemies = Group()
        self.towers = Group()
        self.all_sprites = Group()

    def spawn_enemies(self):
        """Spawns enemies based on enemy_count and how much time has passed since last spawn
        """
        time = pygame.time.get_ticks()
        if self.enemy_count < self.wave_nro * 5:
            if time - self.last_enemy_spawn >= self.enemy_spawn_interval:

                enemy = Enemies(self.route[0])
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)
                self.last_enemy_spawn = time
                self.enemy_count += 1

        elif self.enemy_count == self.wave_nro * 5:
            if time - self.last_enemy_spawn >= 10000:
                self.reset_wave()
                self.advance_wave()

    def reset_wave(self):
        """Resets enemy_count and last_enemy_spawn
        """
        self.enemy_count = 0
        self.last_enemy_spawn = pygame.time.get_ticks()

    def advance_wave(self):
        """Raises the wave number by one
        """
        self.wave_nro += 1

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

    def add_tower(self, x, y):
        """Adds a tower using the x and y values

        Args:
            x : x coordinate of the tower
            y : y coordinate of the tower
        """

        tower = Tower(x, y)
        if x < self.game_width - (tower.rect.width//2) and y < self.game_height - (tower.rect.height//2):

            if self.valid_tower(tower):
                self.towers.add(tower)
                self.all_sprites.add(tower)

    def assign_targets(self, tower):
        """Assigns a enemy as a target for a tower

        Args:
            tower: tower object
        """
        for enemy in self.enemies:
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

        font = pygame.font.SysFont("Arial", 32)
        health_text = font.render("Health: {}".format(
            self.health), True, (255, 255, 255))
        display.blit(health_text, (815, 10))

        self.all_sprites.draw(display)

    def update(self):
        self.spawn_enemies()
        self.enemies.update(self.route)
        self.towers.update(pygame.time.get_ticks(),
                           self.enemies, self.all_sprites)

        for enemy in self.enemies:
            if enemy.reached_end(self.route):
                self.health -= 1
                self.enemies.remove(enemy)
                self.all_sprites.remove(enemy)

        for tower in self.towers:
            if tower.target is None:
                self.assign_targets(tower)
