import random
from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


def foo_heuristic(state):
    result = 0
    for column in range(1, 7):
        for row in range(1, 8):
            if (column, row) in state.moves:
                result += best_direction(tuple=(column, row), state=state)
                break
    return result


def best_direction(tuple, state):
    return horizontal(tuple, state) + vertical(tuple, state)


def vertical(tuple, state):
    accumulated_value = 0
    for row in range(tuple[1], 7):
        coordinate = (tuple[0], row)
        if coordinate in state.moves:
            accumulated_value += 100
        if state.board.get(coordinate) == game.to_move(state):
            accumulated_value += 1000
        if state.board.get(coordinate) != game.to_move(state):
            accumulated_value -= 10000
    return accumulated_value


def horizontal(tuple, state):
    accumulated_value = 0
    for column in range(tuple[0], 7):
        coordinate = (column, tuple[1])
        if coordinate in state.moves:
            accumulated_value += 100
        if state.board.get(coordinate) == game.to_move(state):
            accumulated_value += 1000
        if state.board.get(coordinate) != game.to_move(state):
            accumulated_value -= 10000
    return accumulated_value

"""
def posibles_diagonales(state=None):
    acumulated_value = 0

    for columna in range(1, 7):

        if state.board.get((columna, fila)) == ".":
            acumulated_value += 100
        if state.board.get((columna, fila)) == game.to_move(state):
            acumulated_value += 1000
        if state.board.get((columna, fila)) != game.to_move(state):
            acumulated_value -= 10000

    return acumulated_value
"""
