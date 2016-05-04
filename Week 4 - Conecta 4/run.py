import games
from connectfour import ConnectFour
from heuristics import random_heuristic, best_direction, foo_heuristic

# game = games.TicTacToe(h=3,v=3,k=3)
game = ConnectFour()

state = game.initial


def choice_menu():
    global computer
    choice = raw_input("Elije quien empieza: 0 -> tu, 1 -> maquina")
    computer = 'O' if choice == '0' else 'X'

choice_menu()

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
        move = games.alphabeta_search(state, game, eval_fn=foo_heuristic)

        state = game.make_move(move, state)
        computer = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
