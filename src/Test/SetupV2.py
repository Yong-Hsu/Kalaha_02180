import copy
import math
import random

from main import print_game
from src.AI.MiniMaxAlphaBetav2 import minimax


# Game played using MiniMaxAlphaBetav2
class Setup:
    def Play(self, game, depth, isPrint=False):
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
                tempGame = copy.deepcopy(game)
                slot, _ = minimax(game=tempGame, depth=depth, turn=1, alpha=-math.inf, beta=math.inf)

            # Reverse slot if player 2 is playing
            game.take_slot(slot)
