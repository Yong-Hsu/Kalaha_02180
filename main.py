from src.kalaha import Game

"""
This is the main script which runs the game with one player and one AI.

The human player starts.
"""


def print_game(game):
    # Command-line textual representation of the game
    state = game.get_state()
    slots = list(range(0, 6))
    player1_state = state[0]
    player2_state = state[1]
    player2_state.reverse()

    print("Slots:   | ", end="");
    print(*slots, sep=" | ", end="");
    print(" |")
    print("=======================================")
    print("Player 2 | ", end="")
    print(*player2_state[1:], sep=" | ", end="");
    print(" | Score: {0}".format(player2_state[0]))
    print("---------------------------------------")
    print("Player 1 | ", end="")
    print(*player1_state[0:-1], sep=" | ", end="");
    print(" | Score: {0}".format(player1_state[-1]))
    print("=======================================")


def check_input(str):
    while 1:
        try:
            val = int(input(str))
            break
        except ValueError:
            print("Not a recognizable integer, please try again.")

    return val


if __name__ == "__main__":
    # Run game
    game = Game()
    should_end = game.is_terminal_state()

    print("Running game (counter-clockwise)")
    game_seq = []
    while not should_end:
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
            print("")

        game_seq.append((player_turn, slot))
        # Reverse slot if player 2 is playing
        game.take_slot(slot)

        winner = 0
        if game.is_terminal_state():
            winner = game.end_game()
            should_end = True
            print_game(game)

    print("Game over, winner is Player {0}".format(winner))
    print("Game sequence:", game_seq)
    input("Press Enter to end...")
