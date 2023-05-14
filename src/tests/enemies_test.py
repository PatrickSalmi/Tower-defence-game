import unittest
import pygame
from sprites.enemies import Enemies
from gamelogic.tower_defence import TowerDefence


class TestEnemies(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemies((100, 200))

    def test_correct_starting_position(self):
        self.assertEqual(self.enemy.rect.centerx, 100)
        self.assertEqual(self.enemy.rect.centery, 200)
        
    def test_fast_enemy(self):
        enemy = Enemies((0,0), "fast")
        
        self.assertEqual(enemy.speed, 4)
        
    def test_take_damage(self):
        self.enemy.take_damage(pygame.time.get_ticks())
        
        self.assertEqual(self.enemy.image, self.enemy.damage_image)
        
    def test_initial_movement(self):
        game = TowerDefence()
        route = game.route
        enemy = Enemies(route[0])
        
        enemy.update(route)
        
        self.assertEqual(enemy.rect.centerx, route[enemy.index][0])
