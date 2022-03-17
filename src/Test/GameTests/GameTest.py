import unittest

from src.Test.Setup import Setup
from src.kalaha import Game


class GameTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.iterations = 30

    def test_game(self):
        for i in range(self.iterations):
            with self.subTest():
                winner = Setup.Play(Game(), depth=5)
                self.assertEqual(2, winner)
