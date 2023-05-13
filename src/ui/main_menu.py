import pygame
from ui.buttons import Buttons
from load_image import load_image

class MainMenu():
    
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 28)
        
        self.play_button = Buttons(580, 300, load_image("play.png"))
        
    def draw_all(self, display):
        display.fill((165, 189, 137))
        self.play_button.draw(display)