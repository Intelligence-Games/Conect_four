import random
from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


def foo_heuristic(state):
    result = 0
    for columna in range(1, 7):
        for fila in range(1, 8):
            if (columna, fila) in state.moves:
                result += best_direction(tupla=(columna,fila), state=state)
                break
    return result


def best_direction(tupla=None, state=None):
    return posibles_horizontales(tupla, state) + posibles_verticales(tupla, state)

def posibles_verticales(tupla, state=None):
    acumulated_value = 0

    for fila in range(tupla[1], 7):
        if (tupla[0], fila) in state.moves:
            acumulated_value += 100

        if state.board.get((tupla[0], fila)) == game.to_move(state):
            acumulated_value += 1000
        if state.board.get((tupla[0], fila)) != game.to_move(state):
            acumulated_value -= 10000
    return acumulated_value


def posibles_horizontales(tupla, state=None):
    acumulated_value = 0
    num = tupla[0]
    for columna in range(tupla[0], 7):
        if (columna, tupla[1]) in state.moves:
            acumulated_value += 100
        if state.board.get((columna, tupla[1])) == game.to_move(state):
            acumulated_value += 1000
        if state.board.get((columna, tupla[1])) != game.to_move(state):
            acumulated_value -= 10000

    return acumulated_value

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