import unittest

from src.Test.SetupV2 import Setup
from src.kalaha import Game


class GameTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.iterations = 3

    def test_game(self):
        for i in range(self.iterations):
            with self.subTest():
                newGame = Game(state={0: [4] * 6 + [0], 1: [4] * 6 + [0]})
                winner = Setup.Play(self, game=newGame, depth=4)
                self.assertEqual(2, winner)
