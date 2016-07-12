import games
from connectfour import ConnectFour
from heuristics import random_heuristic, best_direction, best_move_heuristic

# game = games.TicTacToe(h=3,v=3,k=3)
game = ConnectFour()

state = game.initial


def choice_level():
    global heuristic
    global depth
    level = raw_input("Elije la dificultad: 1 -> facil, 2 -> medio, 3 -> dificil: ")
    if level == '1':
        heuristic = random_heuristic
        depth = None
    elif level == '2':
        heuristic = best_move_heuristic
        depth = None
    else:
        heuristic = best_move_heuristic
        depth = 4


def choice_turn():
    global computer
    choice = raw_input("Elije ficha: 0 -> O, 1 -> X = ")
    computer = 'X' if choice == '0' else 'O'

choice_level()
choice_turn()

while True:

    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if computer == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        computer = 'X'
    else:
        print "Thinking..."
        # move = games.minimax_decision(state, game)
        # move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game, depth, eval_fn=heuristic)

        state = game.make_move(move, state)
        computer = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
