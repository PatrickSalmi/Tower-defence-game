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
        self.speed = 1
        self.index = 1

    def reached_end(self, path_line):
        return self.rect.centerx >= path_line[-1][0] and self.rect.centery >= path_line[-1][1]

    def update(self, path_line):
        if self.index < len(path_line):
            next_x, next_y = path_line[self.index]
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
