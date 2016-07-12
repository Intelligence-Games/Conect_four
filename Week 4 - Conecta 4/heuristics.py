import random

from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


def memoize(heuristic):
    memory = {}

    def helper(state):
        if str(state.board) not in memory:
            memory[str(state.board)] = heuristic(state)
        return memory[str(state.board)]

    return helper


@memoize
def best_move_heuristic(state=None):
    result = 0

    if state.utility == 1:
        return state.utility * 10000000
    if state.utility == -1:
        return state.utility * 5000000

    for column in range(1, 7):
        for row in range(1, 8):
            if (column, row) in state.moves:
                result += best_direction(coordinate=(column, row), state=state)
                break
    return result


def best_direction(coordinate, state):
    return horizontal(coordinate, state) \
           + vertical(coordinate, state) \
           + diagonal(coordinate, state) \
           + inverse_diagonal(coordinate, state)


values = {
    0: 0,
    1: 100,
    2: 1000,
    3: 10000
}


def calculate_neighbours(coordinate, state, action):
    player = state.board.get(action(coordinate))
    in_row = calculate_in_row(player=player, state=state, coordinate=coordinate)

    player_value = values[in_row] if (player == game.to_move(state)) else -values[in_row]
    return player_value


def vertical(coordinate, state):
    bottom = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0], coordinate[1] - 1))
    top = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0], coordinate[1] + 1))
    return bottom + top


def horizontal(coordinate, state):
    right = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0]+1, coordinate[1]))
    left = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0]-1, coordinate[1]))
    return right + left


def diagonal(coordinate, state):
    top_right = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0] + 1, coordinate[1] + 1))
    bottom_left = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0] - 1, coordinate[1] - 1))
    return top_right + bottom_left


def inverse_diagonal(coordinate, state):

    top_left = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0] - 1, coordinate[1] + 1))
    bottom_right = calculate_neighbours(coordinate, state, lambda coordinate_parameter: (coordinate[0] + 1, coordinate[1] - 1))
    return top_left + bottom_right




def calculate_in_row(player, state, coordinate):
    board = state.board
    in_row = 0
    if player is not None:
        index = 1
        while index < 4:
            if board.get((coordinate[0] - index, coordinate[1])) == player or \
                            board.get((coordinate[0] + index, coordinate[1])) == player or \
                            board.get((coordinate[0], coordinate[1] - index)) == player or \
                            board.get((coordinate[0], coordinate[1] + index)) == player or \
                            board.get((coordinate[0] + index, coordinate[1] - index)) == player or \
                            board.get((coordinate[0] - index, coordinate[1] + index)) == player or \
                            board.get((coordinate[0] + index, coordinate[1] + index)) == player or \
                            board.get((coordinate[0] - index, coordinate[1] - index)) == player:
                in_row += 1
            else:
                if (coordinate[0] - index, coordinate[1]) in state.moves:
                    pass
                else:
                    break
            index += 1
    return in_row
