import unittest
from gamelogic.tower_defence import TowerDefence
from sprites.enemies import Enemies
from sprites.towers import Tower


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TowerDefence()

    def test_advance_wave(self):
        self.game.waves.advance_wave()
        self.assertEqual(self.game.waves.wave_nro, 2)

    def test_add_tower(self):
        self.game.place_tower((200, 500))
        self.assertEqual(len(self.game.towers), 1)

    def test_adding_tower_on_route(self):
        self.game.place_tower((50, 200))
        self.assertEqual(len(self.game.towers), 0)

    def test_adding_tower_on_exsisting_tower(self):
        tower = Tower((200, 500))
        self.game.towers.add(tower)

        self.game.place_tower((200, 500))

        self.assertEqual(len(self.game.towers), 1)

    def test_adding_enemy(self):
        enemy = Enemies(self.game.route[0])
        self.game.waves.enemies.add(enemy)
        self.assertEqual(len(self.game.waves.enemies), 1)

    def test_calculate_score(self):
        self.game.calculate_score()
        correct_score = (self.game.waves.wave_nro * 20) + (self.game.health *
                                                           self.game.waves.wave_nro * 5) + (self.game.money * 2)

        self.assertEqual(self.game.score, correct_score)

    def test_end_game_method(self):
        self.game.end_game()

        self.assertEqual(self.game.game_over, True)

    def test_reset_game(self):
        self.game.score = 100
        self.game.reset_game()

        self.assertEqual(self.game.score, 0)

    def test_sell_tower(self):
        tower = Tower((0, 0))
        self.game.sell_tower(tower)

        self.assertEqual(self.game.money, 35)

    def test_assign_targets(self):
        tower = Tower((0, 0))
        enemy = Enemies((0, 0))

        self.game.waves.enemies.add(enemy)
        self.game.assign_targets(tower)

        self.assertEqual(tower.target, enemy)

    def test_reassing_target(self):
        tower = Tower((0, 0))
        enemy = Enemies((0, 0))
        enemy2 = Enemies((0, 0))
        enemy2.index = 2

        self.game.waves.enemies.add(enemy)
        self.game.assign_targets(tower)
        self.game.waves.enemies.add(enemy2)
        self.game.assign_targets(tower)

        self.assertEqual(tower.target, enemy2)

    def test_toggle_pause(self):
        self.game.toggle_pause()

        self.assertEqual(self.game.pause, True)

    def test_killing_enemy(self):
        enemy = Enemies((0, 0))
        enemy2 = Enemies((0, 0))
        self.game.waves.enemies.add(enemy)
        self.game.waves.enemies.add(enemy2)

        enemy.health = 0
        self.game.update()

        self.assertEqual(len(self.game.waves.enemies), 1)
