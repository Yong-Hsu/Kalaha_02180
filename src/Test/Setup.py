import copy
import math
import random

from main import print_game
from src.AI.MiniMaxAlphaBeta import minimax

class Setup:
    def Play(game, depth, isPrint=False):
        while True:
            if game.is_terminal_state():
                winner = game.end_game()
                print_game(game)
                return winner

            if isPrint:
                print_game(game)
                print("\n")

            player_turn = game.get_player_turn()
            # get slot choice from player or AI
            slot = None
            if player_turn == 0:
                # Player
                slot = random.randint(0, 5)
            else:
                # AI
                slot, _ = minimax(copy.deepcopy(game), depth=depth, turn=1, alpha=-math.inf, beta=math.inf)

            # Reverse slot if player 2 is playing
            game.take_slot(slot)


