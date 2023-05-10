import pygame
from load_image import load_image


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load_image("tower.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.range = 300
        self.cooldown = 4000
        self.last_attack_time = 0
        self.target = None

    def update(self, current_time, enemies):
        if self.target:
            if enemies and current_time - self.last_attack_time >= self.cooldown:
                enemies.remove(self.target)
                self.last_attack_time = current_time
            else:
                self.target = None
                
    def calculate_distance(self, enemy):
        distance = (enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2
        if distance <= self.range **2:
            self.target = enemy
                
    
