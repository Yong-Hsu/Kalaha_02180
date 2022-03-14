import copy
import math


# minimax(game, depth=5, turn=1, alpha=-math.inf, beta=math.inf)
def minimax(game, depth, turn, alpha, beta):
    move = -1

    if depth == 0 | game.is_terminal_state():
        return move, evaluation(game)

    if turn == 1:
        max_eval = -math.inf
        for i in range(6):
            game_temp = copy.deepcopy(game)
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                _, eval_compare = minimax(game_temp, depth - 1, 0, alpha, beta)
                # max_eval = max(max_eval, eval_compare)
                if max_eval <= eval_compare:
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
                _, eval_compare = minimax(game_temp, depth - 1, 1, alpha, beta)
                # min_eval = min(min_eval, eval_compare)
                if min_eval >= eval_compare:
                    min_eval = eval_compare
                    move = i
                beta = min(beta, eval_compare)
                if beta <= alpha:
                    break
        return move, min_eval


# evaluation of
def evaluation(game):
    state = game.get_state()
    # turn = game.get_player_turn()

    # implement stealing and same_turn later, we need information from the last state
    delta_pieces = state[0][-1] - state[1][-1]

    # todo: about terminal state
    # todo: implement stealing and same_turn later, we need information from the last state

    return delta_pieces

