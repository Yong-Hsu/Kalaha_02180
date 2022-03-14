import copy
import math


def minimax0(game, depth, turn):
    # depth bigger than 0
    game_temp = copy.deepcopy(game)

    move = -1

    if depth == 0 | game_temp.is_terminal_state():
        return move, evaluation(game_temp)

    if turn == 1:
        max_eval = -math.inf
        for i in range(6):
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                _, eval_compare = minimax0(game_temp, depth - 1, 0)
                # max_eval = max(max_eval, eval_compare)
                if max_eval <= eval_compare:
                    max_eval = eval_compare
                    move = i
        return move, max_eval
    else:
        min_eval = math.inf
        for i in range(6):
            is_valid_move = game_temp.take_slot(i)
            if is_valid_move:
                _, eval_compare = minimax0(game_temp, depth - 1, 1)
                # min_eval = min(min_eval, eval_compare)
                if min_eval >= eval_compare:
                    min_eval = eval_compare
                    move = i
        return move, min_eval


# evaluation of
def evaluation(game):
    state = game.get_state()
    # turn = game.get_player_turn()

    # the pieces they can have
    delta_pieces = state[0][-1] - state[1][-1]

    return delta_pieces

# from src.kalaha import Game
# game = Game()
# import math
# game.take_slot(1)
# game.take_slot(2)
# game.take_slot(3)
# game.take_slot(3)
# from src.AI.Minimax import minimax0
# slot, eval = minimax0(game, depth=3, turn=1)
