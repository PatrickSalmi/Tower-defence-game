import unittest
from gamelogic.tower_defence import TowerDefence
from gamelogic.enemies import Enemies


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TowerDefence()
        
    def test_advance_wave(self):
        self.game.advance_wave()
        self.assertEqual(self.game.wave_nro, 2)
        
    def test_add_tower(self):
        self.game.add_tower(50, 50)
        self.assertEqual(len(self.game.towers), 1)
        
    def test_adding_tower_on_route(self):
        self.game.add_tower(50,200)
        self.assertEqual(len(self.game.towers), 0)
        
    def test_adding_enemy(self):
        enemy = Enemies(self.game.route[0])
        self.game.enemies.append(enemy)
        self.assertEqual(len(self.game.enemies), 1)