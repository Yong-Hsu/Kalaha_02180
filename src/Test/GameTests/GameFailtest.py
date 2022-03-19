import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameFailTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [1] + [0] * 5 + [0], 1: [0] * 6 + [0]}
        cls.game = Game(state=gameBoard)

    def test_Fail(self):
        winner = Setup.Play(self, game=self.game, depth=5, isPrint=True)
        self.assertEqual(1, winner)
