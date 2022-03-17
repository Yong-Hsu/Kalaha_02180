import math
import unittest
from src import Game
from src.AI.MiniMaxAlphaBeta import minimax


# Terminal moves can be broken into two: A terminal move resulting in the AI winning and the opposite.
# The former should be prioritized over all other move types and the later should be prioritized the lowest of all
# move types.


class EvaluationTerminalMoves(unittest.TestCase):

    @classmethod
    def setUp(cls):
        gameBoard = {0: [0, 2, 1, 1, ], 1: [0] * 5 + [1] + [0]} # Todo: Assign gameboard such that we have terminal moves, one that wins the game, and one that loses the game
        cls.game = Game(state=gameBoard, player_turn=1)

    def test_TerminalWin(self):
        slot, _ = minimax(self.game, depth=1, turn=1, alpha=-math.inf, beta=math.inf)
        self.assertEqual(slot, 1)  # Actual = slot that results in a terminal win move

    def test_TerminalLose(self):
        slot, _ = minimax(self.game, depth=1, turn=1, alpha=-math.inf, beta=math.inf)
        self.assertEqual(slot, 1)  # Actual = slot that results in a terminal win lose
