import pygame
from gamelogic.enemies import Enemies


class TowerDefence():
    def __init__(self):
        self.route = [(50, 0), (50, 200), (400, 200),
            (400, 400), (800, 400), (800, 720)]
        self.enemy = Enemies(self.route[0])
        self.path_line = [(x-self.enemy.width//2, y-self.enemy.height//2) for x, y in self.route]
        self.wave_nro = 1
        self.enemies = []
        self.enemy_count = 0
        self.enemy_spawn_interval = 2000
        self.last_enemy_spawn = pygame.time.get_ticks()

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

    def update_enemies(self, screen):
        pygame.draw.lines(screen, (128, 128, 128), False, self.route, 20)
        for enemy in self.enemies:
            enemy.draw(screen)
            enemy.pathing(self.path_line)
