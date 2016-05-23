import random

from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


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


def calculate_in_row(player, state, coordinate):
    board = state.board
    in_row = 0
    if player is not None:
        index = 1
        while index < 4:
            if board.get((coordinate[0] - index, coordinate[1])) == player:
                in_row += 1
            else:
                if (coordinate[0] - index, coordinate[1]) in state.moves:
                    pass
                else:
                    break
            index += 1
    return in_row


def vertical(coordinate, state):
    coordinate_x = coordinate[0]
    coordinate_y = coordinate[1]

    bottom_player = state.board.get((coordinate_x, coordinate_y - 1))
    top_in_row = calculate_in_row(player=bottom_player, state=state, coordinate=coordinate)

    top_player = state.board.get((coordinate_x, coordinate_y + 1))
    bottom_in_row = calculate_in_row(player=top_player, state=state, coordinate=coordinate)

    total_value = 0
    if bottom_player == game.to_move(state):
        total_value += values[bottom_in_row]
    else:
        total_value -= values[bottom_in_row]

    if top_player == game.to_move(state):
        total_value += values[top_in_row]
    else:
        total_value -= values[top_in_row]

    return total_value


def horizontal(coordinate, state):
    coordinate_x = coordinate[0]
    coordinate_y = coordinate[1]

    left_player = state.board.get((coordinate_x - 1, coordinate_y))
    left_in_row = calculate_in_row(player=left_player, state=state, coordinate=coordinate)

    right_player = state.board.get((coordinate_x + 1, coordinate_y))
    right_in_row = calculate_in_row(player=right_player, state=state, coordinate=coordinate)

    total_value = 0
    if left_player == game.to_move(state):
        total_value += values[left_in_row]
    else:
        total_value -= values[left_in_row]

    if right_player == game.to_move(state):
        total_value += values[right_in_row]
    else:
        total_value -= values[right_in_row]

    return total_value


def diagonal(coordinate, state):
    coordinate_x = coordinate[0]
    coordinate_y = coordinate[1]

    top_right_player = state.board.get((coordinate_x + 1, coordinate_y + 1))
    top_right_in_row = calculate_in_row(player=top_right_player, state=state, coordinate=coordinate)

    left_bottom_player = state.board.get((coordinate_x - 1, coordinate_y - 1))
    left_bottom_in_row = calculate_in_row(player=left_bottom_player, state=state, coordinate=coordinate)

    total_value = 0
    if left_bottom_player == game.to_move(state):
        total_value += values[left_bottom_in_row]
    else:
        total_value -= values[left_bottom_in_row]

    if top_right_player == game.to_move(state):
        total_value += values[top_right_in_row]
    else:
        total_value -= values[top_right_in_row]

    return total_value


def inverse_diagonal(coordinate, state):
    coordinate_x = coordinate[0]
    coordinate_y = coordinate[1]

    top_left_player = state.board.get((coordinate_x - 1, coordinate_y + 1))
    top_left_in_row = calculate_in_row(player=top_left_player, state=state, coordinate=coordinate)

    right_bottom_player = state.board.get((coordinate_x + 1, coordinate_y - 1))
    right_bottom_in_row = calculate_in_row(player=right_bottom_player, state=state, coordinate=coordinate)

    total_value = 0
    if top_left_player == game.to_move(state):
        total_value += values[top_left_in_row]
    else:
        total_value -= values[top_left_in_row]

    if right_bottom_player == game.to_move(state):
        total_value += values[right_bottom_in_row]
    else:
        total_value -= values[right_bottom_in_row]

    return total_value
