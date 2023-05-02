import pygame
from load_image import load_image

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = load_image("tower.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        pass
        
        