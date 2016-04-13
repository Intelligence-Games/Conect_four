"""Games, or Adversarial Search. (Chapters 6)

"""

from utils import *
from searches import alphabeta_search


# ______________________________________________________________________________
# Players for Games

def query_player(game, state):
    "Make a move by querying standard input."
    # game.display(state)
    return num_or_str(raw_input('Your move? '))


def random_player(game, state):
    "A player that chooses a legal move at random."
    return random.choice(game.legal_moves(state))


def alphabeta_player(game, state):
    return alphabeta_search(state, game)


def play_game(game, *players):
    "Play an n-person, move-alternating game."
    state = game.initial
    while True:
        for player in players:
            move = player(game, state)
            print player, move
            state = game.make_move(move, state)
            if game.terminal_test(state):
                print game.display(state)
                return game.utility(state, 'X')
