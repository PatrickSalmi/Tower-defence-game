import pygame
from load_image import load_image


class Enemies(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()

        self.image = load_image("robo.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.speed = 2
        self.index = 1

    def reached_end(self, route):
        return self.rect.centerx >= route[-1][0] and self.rect.centery >= route[-1][1]

    def update(self, route):
        if self.index < len(route):
            next_x, next_y = route[self.index]
            if self.rect.centerx < next_x:
                self.rect.centerx += self.speed
            elif self.rect.centerx > next_x:
                self.rect.centerx -= self.speed
            elif self.rect.centery < next_y:
                self.rect.centery += self.speed
            elif self.rect.centery > next_y:
                self.rect.centery -= self.speed
            else:
                self.index += 1
