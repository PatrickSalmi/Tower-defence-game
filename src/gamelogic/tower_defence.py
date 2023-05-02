import pygame
from gamelogic.enemies import Enemies
from gamelogic.towers import Tower


class TowerDefence():
    def __init__(self):
        self.route = [(50, 0), (50, 200), (400, 200),
                      (400, 400), (800, 400), (800, 720)]

        self.route_rect = []

        for i in range(len(self.route) - 1):
            start = self.route[i]
            end = self.route[i+1]
            line_rect = pygame.Rect(
                start, (end[0]-start[0], end[1]-start[1]+30))
            self.route_rect.append(line_rect)

        self.enemy = Enemies(self.route[0])
        self.path_line = [(x-self.enemy.width//2, y-self.enemy.height//2)
                          for x, y in self.route]
        self.wave_nro = 1
        self.enemies = []
        self.enemy_count = 0
        self.enemy_spawn_interval = 2000
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.health = 5

        self.towers = []

    def spawn_enemies(self):
        time = pygame.time.get_ticks()
        if self.enemy_count < self.wave_nro * 5:
            if time - self.last_enemy_spawn >= self.enemy_spawn_interval:

                enemy = Enemies(self.route[0])
                self.enemies.append(enemy)
                self.last_enemy_spawn = time
                self.enemy_count += 1

        elif self.enemy_count == self.wave_nro * 5:
            if time - self.last_enemy_spawn >= 10000:
                self.reset_wave()
                self.advance_wave()

    def reset_wave(self):
        self.enemy_count = 0
        self.last_enemy_spawn = pygame.time.get_ticks()

    def advance_wave(self):
        self.wave_nro += 1

    def valid_tower(self, tower_rect):
        for line in self.route_rect:
            if line.colliderect(tower_rect):
                return False
        return True

    def add_tower(self, x, y):
        tower = Tower(x, y)
        tower_rect = tower.rect.move(
            x - tower.rect.centerx, y - tower.rect.centery)
        if self.valid_tower(tower_rect):
            tower.rect.center = (x, y)
            self.towers.append(tower)

    def draw_all(self, display):
        display.fill((0, 128, 0))
        pygame.draw.lines(display, (128, 128, 128), False, self.route, 20)

        font = pygame.font.SysFont("Arial", 32)
        health_text = font.render("Health: {}".format(
            self.health), True, (255, 255, 255))
        display.blit(health_text, (815, 10))

        for enemy in self.enemies:
            enemy_rect = enemy.rect.move(enemy.x, enemy.y)
            enemy.update(self.path_line)
            display.blit(enemy.image, enemy_rect)

            if enemy.reached_end(self.path_line):
                self.health -= 1
                self.enemies.remove(enemy)

        for tower in self.towers:
            display.blit(tower.image, tower.rect)
