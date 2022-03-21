import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.iterations = 30
        cls.results = []

    def test_game(self):
        for i in range(self.iterations):
            with self.subTest():
                newGame = Game(state={0: [4] * 6 + [0], 1: [4] * 6 + [0]})
                winner = Setup.Play(self, game=newGame, depth=5)
                self.results.append(winner)
        wincount = self.results.count(2)
        self.assertGreater(wincount, self.iterations * 0.8)  # Assert that AI wins at least 80% of games
