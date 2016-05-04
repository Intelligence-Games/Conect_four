import games
from connectfour import ConnectFour
from heuristics import Heuristics

# game = games.TicTacToe(h=3,v=3,k=3)
game = ConnectFour()
state = game.initial
heuristics = Heuristics()


def choice_level():
    global heuristic
    global depth
    level = raw_input("Elije la dificultad: 1 -> facil, 2 -> medio, 3 -> dificil: ")
    if level == '1':
        heuristic = heuristic.random_heuristic
        depth = None
    elif level == '2':
        heuristic = heuristics.best_move_heuristic
        depth = None
    else:
        heuristic = heuristics.best_move_heuristic
        depth = 4


def choice_turn():
    global computer
    choice = raw_input("Elije quien empieza: 0 -> tu, 1 -> maquina: ")
    computer = 'O' if choice == '0' else 'X'

# choice_level()
# choice_turn()

computer = "X"

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
        move = games.alphabeta_search(state, game, d=4, eval_fn=heuristics.best_move_heuristic)

        state = game.make_move(move, state)
        computer = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
