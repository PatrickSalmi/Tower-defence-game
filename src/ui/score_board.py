import pygame
from ui.buttons import Buttons
from load_image import load_image
from scores import load_scores


class ScoreBoard():

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 28)
        self.load_scores()

        self.back_button = Buttons(30, 640, load_image("back.png"))

    def draw_all(self, display):
        display.fill((118, 109, 103))

        high_scores_text = self.font.render(
            "High Scores", True, (255, 255, 255))
        display.blit(high_scores_text, (558, 100))

        score_y = 150

        for i in range(10):
            if i < len(self.scores):
                score = self.scores[i]
                score_text = self.font.render(
                    f"{i+1}. {score}", True, (255, 255, 255))
            else:
                score_text = self.font.render(
                    f"{i+1}. ...", True, (255, 255, 255))

            if i == 9:
                display.blit(score_text, (584, score_y))

            else:
                display.blit(score_text, (600, score_y))
            score_y += 30

        self.back_button.draw(display)

    def load_scores(self):
        self.scores = load_scores()
