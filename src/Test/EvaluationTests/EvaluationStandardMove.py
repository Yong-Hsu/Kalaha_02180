import math
import unittest

from main import print_game
from src import Game
from src.AI.MiniMaxAlphaBeta import minimax


class EvaluationStandardMove(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [3, 3, 3, 1, 0, 0] + [0], 1: [4, 3, 2, 4, 3, 5] + [0]}
        cls.game = Game(state=gameBoard, player_turn=1)
        print_game(cls.game)

    def test_standardMove(self):
        slot, _ = minimax(self.game, depth=1, turn=1, alpha=-math.inf, beta=math.inf)
        self.assertEqual(slot, 5)  # Actual = slot that results in a standard move
