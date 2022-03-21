import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameOnesTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [1] * 6 + [0], 1: [1] * 6 + [0]}
        cls.game = Game(state=gameBoard)

    def test_ones(self):
        winner = Setup.Play(self, self.game, depth=5)
        self.assertEqual(2, winner)  # AI wins
