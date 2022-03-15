import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.game = Game()

    def test_game(self):
        winner = Setup.Play(self.game, depth=5)
        self.assertEqual(2, winner)
