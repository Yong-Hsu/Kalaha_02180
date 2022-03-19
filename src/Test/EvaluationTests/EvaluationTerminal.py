import math
import unittest

from src import Game
from src.AI.Evaluation import evaluation_move


class EvaluationTerminal(unittest.TestCase):

    def test_terminalwin(self):
        gameBoard = {0: [0] * 5 + [1] + [22], 1: [0] * 5 + [1] + [24]}
        game = Game(state=gameBoard, player_turn=1)
        game.take_slot(5)
        state = game.get_state()
        delta_pieces = state[1][-1] - state[0][-1]
        score = evaluation_move(game)
        self.assertEqual(score, delta_pieces * 4)

    def test_terminallossORdraw(self):
        gameBoard = {0: [0] * 5 + [1] + [24], 1: [0] * 5 + [1] + [22]}
        game = Game(state=gameBoard, player_turn=1)
        game.take_slot(5)
        score = evaluation_move(game)
        self.assertEqual(score, 0)
