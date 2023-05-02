import pygame
from load_image import load_image


class Enemies(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()

        self.image = load_image("robo.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.x = start_pos[0] - self.width // 2
        self.y = start_pos[1] - self.height // 2
        self.speed = 1
        self.index = 1
        
    def reached_end(self, path_line):
        return self.x >= path_line[-1][0] and self.y >= path_line[-1][1]

    def update(self, path_line):

        if self.index < len(path_line):
            next_x, next_y = path_line[self.index]
            if self.x < next_x:
                self.x += self.speed
            elif self.x > next_x:
                self.x -= self.speed
            elif self.y < next_y:
                self.y += self.speed
            elif self.y > next_y:
                self.y -= self.speed
            else:
                self.index += 1
