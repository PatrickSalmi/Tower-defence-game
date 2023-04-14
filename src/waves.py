import pygame
from sprites.enemies import Enemies


class Waves():
    def __init__(self):
        self.wave_nro = 1
        self.enemies = []
        self.enemy_count = 0
        self.enemy_spawn_interval = 2000
        self.last_enemy_spawn = pygame.time.get_ticks()

    def spawn_enemies(self, start_pos):
        time = pygame.time.get_ticks()
        if self.enemy_count < self.wave_nro * 5:
            if time - self.last_enemy_spawn >= self.enemy_spawn_interval:
                
                enemy = Enemies(start_pos)
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
    
    def update_enemies(self, screen, path_line):
        for enemy in self.enemies:
            enemy.draw(screen)
            enemy.pathing(path_line)
