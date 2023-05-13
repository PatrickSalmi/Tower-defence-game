import pygame
from sprites.enemies import Enemies


class Waves:
    def __init__(self):
        self.wave_enemy_count = [3, 5, 8, 12, 15, 18, 20, 23, 25, 30]
        self.wave_nro = 1
        self.total_waves = 3
        self.enemy_spawn_interval = 500
        self.wave_length = 5000
        self.wave_start_time = 0
        self.last_enemy_spawn = 0
        self.enemy_count = 0

        self.start_delay = 5000
        self.first_wave_started = False
        self.enemies = pygame.sprite.Group()

    def update(self, route, all_sprites):
        current_time = pygame.time.get_ticks()

        if not self.first_wave_started:
            if current_time - self.wave_start_time >= self.start_delay:
                self.start_waves(current_time)

        elif self.enemy_count < self.wave_enemy_count[self.wave_nro-1] and current_time - self.last_enemy_spawn >= self.enemy_spawn_interval:
            enemy = Enemies(route[0])
            self.enemies.add(enemy)
            all_sprites.add(enemy)
            self.last_enemy_spawn = current_time
            self.enemy_count += 1
            self.wave_start_time = current_time

        if current_time - self.wave_start_time >= self.wave_length and self.wave_nro < self.total_waves:
            self.advance_wave()

        self.enemies.update(route)

    def start_waves(self, current_time):
        self.wave_start_time = current_time
        self.first_wave_started = True

    def advance_wave(self):
        self.wave_nro += 1
        self.enemy_count = 0
        self.last_enemy_spawn = 0
