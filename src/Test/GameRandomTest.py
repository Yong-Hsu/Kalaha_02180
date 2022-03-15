import random
import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameRandomTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameSetup = [random.randint(0, 5) for i in range(6)]
        gameBoard = {0: gameSetup + [0], 1: gameSetup + [0]}

        cls.game = Game(gameBoard)

    def test_random(self):
        winner = Setup.Play(self.game, depth=5)
        self.assertEqual(2, winner)


