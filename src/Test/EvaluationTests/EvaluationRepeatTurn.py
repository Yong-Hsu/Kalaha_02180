import math
import unittest
from src import Game
from src.AI.MiniMaxAlphaBeta import minimax


class EvaluationRepeatTurn(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [1] * 6 + [0], 1: [1] * 6 + [0]}
        cls.game = Game(state=gameBoard, player_turn=1)

    def test_repeatTurn(self):
        slot, _ = minimax(self.game, depth=1, turn=1, alpha=-math.inf, beta=math.inf)
        self.assertEqual(slot, 5)  # Actual = slot that results in a repeat move
