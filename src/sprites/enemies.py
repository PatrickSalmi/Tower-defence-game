import pygame
from load_image import load_image


class Enemies(pygame.sprite.Sprite):
    def __init__(self, start_pos, enemy_type=None):
        """Class for representing enemies in the game.

        Initializes an enemy with the specified starting position and type.

        Args:
            start_pos (tuple): The starting position (x, y) of the enemy.
            enemy_type (str, optional): The type of enemy. Defaults to None.

        """

        super().__init__()
        self.enemy_type = enemy_type

        if enemy_type == "fast":
            self.image = load_image("fast_enemy.png")
            self.damage_image = load_image("fast_enemy_alt.png")
            self.speed = 4
            self.health = 2

        else:
            self.image = load_image("enemy.png")
            self.damage_image = load_image("enemy_alt.png")
            self.speed = 2
            self.health = 4

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.index = 1
        self.damage_time = 0

    def reached_end(self, route):
        """Checks if the enemy has reached the end of the route.

        Args:
            route (list): The list of points defining the game route.

        Returns:
            bool: True if the enemy has reached the end, False otherwise.

        """

        return self.rect.centerx >= route[-1][0] and self.rect.centery >= route[-1][1]

    def update(self, route):
        """Updates the position of the enemy along the route.

        Args:
            route (list): The list of points defining the game route.

        """

        if self.index < len(route):
            next_x, next_y = route[self.index]
            if abs(self.rect.centerx - next_x) < self.speed:
                self.rect.centerx = next_x
            elif self.rect.centerx < next_x:
                self.rect.centerx += self.speed
            elif self.rect.centerx > next_x:
                self.rect.centerx -= self.speed

            if abs(self.rect.centery - next_y) < self.speed:
                self.rect.centery = next_y
            elif self.rect.centery < next_y:
                self.rect.centery += self.speed
            elif self.rect.centery > next_y:
                self.rect.centery -= self.speed

            if self.rect.centerx == next_x and self.rect.centery == next_y:
                self.index += 1

    def take_damage(self, time):
        """ Changes enemies image to the damaged state.

        Args:
            time (int): The current game time in milliseconds.

        """
        self.image = self.damage_image
        self.damage_time = time

    def check_damage(self, time):
        """Checks if the enemy's damage time has expired and restores its image.

        Args:
            time (int): The current game time in milliseconds.

        """

        if self.damage_time > 0 and time - self.damage_time >= 200:
            if self.enemy_type == "fast":
                self.image = load_image("fast_enemy.png")
            else:
                self.image = load_image("enemy.png")
            self.damage_time = 0
