import unittest
from sprites.enemies import Enemies


class TestEnemies(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemies((100, 200))

    def test_correct_starting_position(self):
        # x = 100 - 50(image width) / 2 = 75
        # y = 200 - 86(image heigth) / 2 = 157
        self.assertEqual(self.enemy.x, 75)
        self.assertEqual(self.enemy.y, 157)
