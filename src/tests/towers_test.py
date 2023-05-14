import unittest
import pygame
from gamelogic.tower_defence import TowerDefence
from sprites.towers import Tower
from sprites.enemies import Enemies


class TestTower(unittest.TestCase):
    
    def setUp(self):
        self.tower = Tower((0,0))
        self.enemy = Enemies((0,0))
        
    def test_sniper_tower(self):
        tower = Tower((0,0), "sniper")
        
        self.assertEqual(tower.price, 20)
        
    def test_tower_attack(self):
        self.tower.target = self.enemy
        self.tower.cooldown = 0
        
        self.assertEqual(self.tower.attack(pygame.time.get_ticks()), True)
        
    def test_tower_cooldown(self):
        self.tower.target = self.enemy
        
        self.assertEqual(self.tower.attack(pygame.time.get_ticks()), False)
        
    def test_tower_calculate_distance_success(self):
        self.tower.calculate_distance(self.enemy)
        
        self.assertEqual(self.tower.target, self.enemy)
        
    def test_tower_calculate_distance_fail(self):
        enemy = Enemies((600,600))
        self.tower.calculate_distance(enemy)
        
        self.assertEqual(self.tower.target, None)
        
    