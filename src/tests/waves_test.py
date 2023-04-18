import unittest
from waves import Waves


class TestEnemies(unittest.TestCase):

    def setUp(self):
        self.wave = Waves()
        
    def test_advance_wave(self):
        self.wave.advance_wave()
        self.assertEqual(self.wave.wave_nro, 2)