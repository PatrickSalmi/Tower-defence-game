import unittest
from sprites.enemies import Enemies


class TestEnemies(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemies((100, 200))

    def test_correct_starting_position(self):
        self.assertEqual(self.enemy.rect.centerx, 100)
        self.assertEqual(self.enemy.rect.centery, 200)
