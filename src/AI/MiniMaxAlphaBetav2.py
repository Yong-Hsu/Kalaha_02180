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
                    max_eval = max(max_eval, minimax(game_temp, depth=depth - 1, turn=1, alpha=alpha, beta=beta)[1])
                else:
                    max_eval = max(max_eval, minimax(game_temp, depth=depth - 1, turn=0, alpha=alpha, beta=beta)[1])
            else:
                continue

            if max_eval >= beta:
                return move, max_eval

            if max_eval > alpha:
                move = i

            alpha = max(alpha, max_eval)

        return move, max_eval

    else:
        min_eval = math.inf
        for i in range(6):
            game_temp = copy.deepcopy(game)
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                if game.isRepeat:
                    min_eval = min(min_eval, minimax(game_temp, depth=depth - 1, turn=0, alpha=alpha, beta=beta)[1])
                else:
                    min_eval = min(min_eval, minimax(game_temp, depth=depth - 1, turn=1, alpha=alpha, beta=beta)[1])
            else:
                continue

            if min_eval <= alpha:
                return move, min_eval

            if min_eval < beta:
                move = i

            beta = min(beta, min_eval)

        return move, min_eval
