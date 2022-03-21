def evaluation(game):
    state = game.get_state()
    delta_pieces = state[1][-1] - state[0][-1]

    return delta_pieces


def evaluation_move(game):
    state = game.get_state()
    delta_pieces = state[1][-1] - state[0][-1]
    if game.is_terminal_state():
        game.end_game()  # We end game and update delta_pieces
        delta_pieces = state[1][-1] - state[0][-1]
        if delta_pieces > 0:  # Terminal win
            score = 4
        else:  # Terminal loss
            score = 0
    elif game.isRepeat:  # Repeat turn
        score = 3
    elif game.isSteal:  # Steal move
        score = 2
    else:  # Standard move
        score = 1

    return delta_pieces * score
