import random
from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


def best_direction(state=None):
    posibilidades = [0, 0, 0]

    posibilidades[0] = posibles_verticales()
    posibilidades[1] = posibles_horizontales()
    posibilidades[2] = posibles_diagonales()

    return devuelve_maximo(posibilidades)


def devuelve_maximo(lista):
    lista.sort()
    return lista[lista.__len__() - 1]


def posibles_verticales(state=None):
    acumulated_value = 0;

    columna = 1
    for fila in range(1, 7):
        if state.board.get(columna, fila) == ".":
            acumulated_value += 100;
        if state.board.get(columna, fila) == game.to_move(state):
            acumulated_value += 1000;
        if state.board.get(columna, fila) != game.to_move(state):
            acumulated_value -= 100;

        columna += 1
        return acumulated_value


def posibles_horizontales(state=None):
    acumulated_value = 0;

    fila = 1
    for columna in range(1, 7):
        if state.board.get(columna, fila) == ".":
            acumulated_value += 100;
        if state.board.get(columna, fila) == game.to_move(state):
            acumulated_value += 1000;
        if state.board.get(columna, fila) != game.to_move(state):
            acumulated_value -= 100;

        fila += 1
        return acumulated_value


def posibles_diagonales(state=None):
    acumulated_value = 0;

    fila = 1
    for columna in range(1, 7):

        if state.board.get(columna, fila) == ".":
            acumulated_value += 100;
        if state.board.get(columna, fila) == game.to_move(state):
            acumulated_value += 1000;
        if state.board.get(columna, fila) != game.to_move(state):
            acumulated_value -= 100;

        columna += 1
        fila += 1
        return acumulated_value