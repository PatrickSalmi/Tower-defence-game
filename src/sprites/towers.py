import pygame
from load_image import load_image


class Tower(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = load_image("tower1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (pos)

        self.price = 10
        self.range = 200
        self.cooldown = 2000
        self.last_attack_time = 0
        self.target = None

    def attack(self, current_time):
        if self.target:
            if current_time - self.last_attack_time >= self.cooldown:
                self.last_attack_time = current_time
                return True
            
            self.target = None
            
        return False

    def calculate_distance(self, enemy):
        distance = (enemy.rect.centerx - self.rect.centerx) ** 2 + \
            (enemy.rect.centery - self.rect.centery) ** 2
        if distance <= self.range ** 2:
            self.target = enemy
