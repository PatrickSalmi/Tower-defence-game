import pygame
from load_image import load_image


class Tower(pygame.sprite.Sprite):
    def __init__(self, pos, tower_type=None):
        """Class for representing towers in the game.

        Initializes a tower with the specified position and type.

        Args:
            pos (tuple): The position (x, y) of the tower.
            tower_type (str, optional): The type of the tower. Defaults to None.

        """

        super().__init__()

        if tower_type == "sniper":
            self.image = load_image("sniper.png")
            self.price = 16
            self.range = 300
            self.cooldown = 3000
            self.damage = 5

        else:
            self.image = load_image("tower1.png")
            self.price = 10
            self.range = 180
            self.cooldown = 1500
            self.damage = 2

        self.rect = self.image.get_rect()
        self.rect.center = (pos)
        self.last_attack_time = 0
        self.clicked = False
        self.target = None

    def attack(self, current_time):
        """Checks if the tower can attack and updates its attack cooldown.

        Args:
            current_time (int): The current game time in milliseconds.

        Returns:
            bool: True if the tower can attack, False otherwise.

        """

        if self.target:
            if current_time - self.last_attack_time >= self.cooldown:
                self.last_attack_time = current_time
                return True

            self.target = None

        return False

    def calculate_distance(self, enemy):
        """Calculates the distance between the tower and an enemy and sets the enemy as the target if it is within range.

        Args:
            enemy (Enemies): The enemy object to calculate the distance to.

        """

        distance = (enemy.rect.centerx - self.rect.centerx) ** 2 + \
            (enemy.rect.centery - self.rect.centery) ** 2
        if distance <= self.range ** 2:
            self.target = enemy

    def draw_range(self, display):
        """Draws the range circle of the tower on the game display.

        Args:
            display: The game display surface to draw on.

        """

        circle_center = self.rect.center
        pygame.draw.circle(display, (0, 0, 0), circle_center, self.range, 1)
