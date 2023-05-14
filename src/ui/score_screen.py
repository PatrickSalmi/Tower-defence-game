import pygame
from ui.buttons import Buttons
from load_image import load_image


class ScoreScreen():

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 28)
        self.image = load_image("score_screen_bg.png")

        self.x = 180
        self.y = 60

        self.back_button = Buttons(self.x+20, 480, load_image("back.png"))

        self.wave_score = 0
        self.health_score = 0
        self.money_score = 0
        self.total_score = 0

    def draw_all(self, display):
        wave_text = self.font.render(
            f"Wave score: {self.wave_score}", True, (255, 255, 255))
        health_text = self.font.render(
            f"Health score: {self.health_score}", True, (255, 255, 255))
        money_text = self.font.render(
            f"Money score: {self.money_score}", True, (255, 255, 255))
        total_text = self.font.render(
            f"Total score: {self.total_score}", True, (255, 255, 255))
        display.blit(self.image, (self.x, self.y))

        display.blit(wave_text, (self.x+190, 180))
        display.blit(health_text, (self.x+190, 215))
        display.blit(money_text, (self.x+190, 250))
        display.blit(total_text, (self.x+190, 285))
        self.back_button.draw(display)

    def get_score(self, wave_nro, health, money, total_score):
        self.wave_score = (wave_nro * 20)
        self.health_score = (health * wave_nro * 5)
        self.money_score = (money * 2)
        self.total_score = total_score
