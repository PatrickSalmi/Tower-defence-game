import pygame
from load_image import load_image

class Enemies(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()

        self.image = load_image("robo.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = start_pos[0] - self.width // 2
        self.y = start_pos[1] - self.height // 2
        self.speed = 1
        self.index = 1

    def pathing(self, path_line):

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

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))