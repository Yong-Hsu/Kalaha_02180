import random
import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameRandomTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.iterations = 3

    def test_random(self):
        for i in range(self.iterations):
            with self.subTest():
                gameSetup = [random.randint(0, 5) for i in range(6)]
                gameBoard = {0: gameSetup + [0], 1: gameSetup + [0]}
                game = Game(state=gameBoard)

                winner = Setup.Play(self, game, depth=5)
                self.assertEqual(2, winner)


