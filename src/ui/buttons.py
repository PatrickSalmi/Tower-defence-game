import pygame

class Buttons():
    
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
            
            
    def draw(self, display):
        display.blit(self.image, self.rect)
        
        