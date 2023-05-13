import pygame
from ui.buttons import Buttons
from load_image import load_image


class IngameMenu():
    
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 28)
        
        self.x = 962
        self.y = 0
        self.rect = (self.x, self.y, 318, 720)
        self.bg_color = (118, 109, 103)
        
        self.buy_tower = Buttons(self.x+20, 600, load_image("tower1.png"))
        self.tower_selected = False
        
        
    def draw_all(self, display, health, money):
        health_text = self.font.render(f"Health: {health}" , True, (255, 255, 255))
        money_text = self.font.render(f"Money: {money}" , True, (255, 255, 255))
        
        
        pygame.draw.rect(display, self.bg_color, self.rect)
        display.blit(health_text, (self.x+20, 10))
        display.blit(money_text, (self.x+150, 10))
        self.buy_tower.draw(display)
        
        
        
        
    
        