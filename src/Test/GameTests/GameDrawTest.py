import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameDrawTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [0] * 6 + [0], 1: [0] * 6 + [0]}
        cls.game = Game(state=gameBoard)

    def test_draw(self):
        winner = Setup.Play(self, self.game, depth=5)
        self.assertEqual(-1, winner)  # AI wins
