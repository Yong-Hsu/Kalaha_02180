from src.kalaha import Game
from src.AI.MiniMaxAlphaBeta import minimax
# from src.AI.Minimax import minimax0
import math
import copy

"""
This is the main script which runs the game with one player and one AI.

The human player starts.
"""


def print_game(game_obj):
    # Command-line textual representation of the game
    state = game_obj.get_state()
    slots = list(range(0, 6))
    player1_state = state[0]
    player2_state = state[1]
    player2_state.reverse()

    print("Slots:   | ", end="")
    print(*slots, sep=" | ", end="")
    print(" |")
    print("=======================================")
    print("Player 2 | ", end="")
    print(*player2_state[1:], sep=" | ", end="")
    print(" | Score: {0}".format(player2_state[0]))
    print("---------------------------------------")
    print("Player 1 | ", end="")
    print(*player1_state[0:-1], sep=" | ", end="")
    print(" | Score: {0}".format(player1_state[-1]))
    print("=======================================")


def check_input(string):
    while 1:
        try:
            val = int(input(string))
            break
        except ValueError:
            print("Not a recognizable integer, please try again.")

    return val


if __name__ == "__main__":
    # Run game
    game = Game()

    print("Easy: 0")
    print("Medium: 1")
    print("Hard: 2")
    print("Very hard (and very slow): 3")
    depth = 4 + check_input("Choose difficulty level: ")

    print("Running game (counter-clockwise)")
    game_seq = []
    while True:
        if game.is_terminal_state():
            winner = game.end_game()
            print_game(game)
            break

        print_game(game)

        player_turn = game.get_player_turn()
        print("\nIt is player {0}'s turn".format(1 + player_turn))

        # get slot choice from player or AI
        slot = None
        if player_turn == 0:
            # Player
            slot = check_input("Choose which slot to pick up (index at 0): ")
        else:
            # AI
            # slot, _ = minimax0(game, depth=3, turn=1)
            slot, _ = minimax(copy.deepcopy(game), depth=depth, turn=1, alpha=-math.inf, beta=math.inf)

            print("AI computing best move:", 5 - slot)

        game_seq.append((player_turn, slot))
        # Reverse slot if player 2 is playing
        game.take_slot(slot)

    if winner == -1:
        print("Game ended in a draw".format(winner))
    else:
        print("Game over, winner is Player {0}".format(winner))

    print("Game sequence:", game_seq)
    input("Press Enter to end...")
