import copy
import math

from src.AI.Evaluation import evaluation, evaluation_move


def minimax(game, depth, turn, alpha, beta):
    move = -1

    if depth <= 0 or game.is_terminal_state():
        return move, evaluation_move(game)

    if turn == 1:
        max_eval = -math.inf
        for i in range(6):
            game_temp = copy.deepcopy(game)
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                if game.isRepeat:
                    _, eval_compare = minimax(game_temp, depth - 1, 1, alpha, beta)
                else:
                    _, eval_compare = minimax(game_temp, depth - 1, 0, alpha, beta)

                if max_eval < eval_compare:
                    max_eval = eval_compare
                    move = i

                alpha = max(alpha, eval_compare)

                if beta <= alpha:
                    break

        return move, max_eval

    else:
        min_eval = math.inf
        for i in range(6):
            game_temp = copy.deepcopy(game)
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                if game.isRepeat:
                    _, eval_compare = minimax(game_temp, depth - 1, 0, alpha, beta)
                else:
                    _, eval_compare = minimax(game_temp, depth - 1, 1, alpha, beta)

                if min_eval > eval_compare:
                    min_eval = eval_compare
                    move = i

                beta = min(beta, eval_compare)

                if beta <= alpha:
                    break

        return move, min_eval
