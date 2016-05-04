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
                result += best_direction(tuple=(column, row), state=state)
                break
    return result


def best_direction(tuple, state):
    return horizontal(tuple, state) + vertical(tuple, state) + diagonal(tuple, state) + inverse_diagonal(tuple, state)


values = {
    0: 0,
    1: 100,
    2: 1000,
    3: 10000
}


def vertical(tuple, state):
    index = 1
    top_in_row = 0
    bottom_in_row = 0
    total_value = 0

    bottom_player = state.board.get((tuple[0], tuple[1] - 1))
    if bottom_player is not None:
        while index < 4:
            if state.board.get((tuple[0], tuple[1] - index)) == bottom_player:
                bottom_in_row += 1
            else:
                break
            index += 1

    index = 1
    top_player = state.board.get((tuple[0], tuple[1] + 1))
    if top_player is not None:
        while index < 4:
            if state.board.get((tuple[0], tuple[1] + index)) == top_player:
                top_in_row += 1
            else:
                break
            index += 1
    if bottom_player == game.to_move(state):
        total_value += values[bottom_in_row]
    else:
        total_value -= values[bottom_in_row]

    if top_player == game.to_move(state):
        total_value += values[top_in_row]
    else:
        total_value -= values[top_in_row]

    return total_value


def horizontal(tuple, state):
    index = 1
    left_in_row = 0
    right_in_row = 0
    total_value = 0

    left_player = state.board.get((tuple[0] - 1, tuple[1]))
    if left_player is not None:
        while index < 4:
            if state.board.get((tuple[0] - index, tuple[1])) == left_player:
                left_in_row += 1
            else:
                break
            index += 1

    index = 1
    right_player = state.board.get((tuple[0] + 1, tuple[1]))
    if right_player is not None:
        while index < 4:
            if state.board.get((tuple[0] + index, tuple[1])) == right_player:
                right_in_row += 1
            else:
                break
            index += 1

    if left_player == game.to_move(state):
        total_value += values[left_in_row]
    else:
        total_value -= values[left_in_row]

    if right_player == game.to_move(state):
        total_value += values[right_in_row]
    else:
        total_value -= values[right_in_row]

    return total_value


def diagonal(tuple, state):
    index = 1
    top_right_in_row = 0
    left_bottom_in_row = 0
    total_value = 0

    top_right_player = state.board.get((tuple[0] + 1, tuple[1] + 1))
    if top_right_player is not None:
        while index < 4:
            if state.board.get((tuple[0] + index, tuple[1] + index)) == top_right_player:
                top_right_in_row += 1
            else:
                break
            index += 1

    index = 1
    left_bottom_player = state.board.get((tuple[0] - 1, tuple[1] - 1))
    if left_bottom_player is not None:
        while index < 4:
            if state.board.get((tuple[0] + index, tuple[1])) == left_bottom_player:
                left_bottom_in_row += 1
            else:
                break
            index += 1

    if left_bottom_player == game.to_move(state):
        total_value += values[left_bottom_in_row]
    else:
        total_value -= values[left_bottom_in_row]

    if top_right_player == game.to_move(state):
        total_value += values[top_right_in_row]
    else:
        total_value -= values[top_right_in_row]

    return total_value


def inverse_diagonal(tuple, state):
    index = 1
    top_left_in_row = 0
    right_bottom_in_row = 0
    total_value = 0

    top_left_player = state.board.get((tuple[0] - 1, tuple[1] + 1))
    if top_left_player is not None:
        while index < 4:
            if state.board.get((tuple[0] - index, tuple[1] + index)) == top_left_player:
                top_left_in_row += 1
            else:
                break
            index += 1

    index = 1
    right_bottom_player = state.board.get((tuple[0] + 1, tuple[1] - 1))
    if right_bottom_player is not None:
        while index < 4:
            if state.board.get((tuple[0] + index, tuple[1] - index)) == right_bottom_player:
                right_bottom_in_row += 1
            else:
                break
            index += 1

    if top_left_player == game.to_move(state):
        total_value += values[top_left_in_row]
    else:
        total_value -= values[top_left_in_row]

    if right_bottom_player == game.to_move(state):
        total_value += values[right_bottom_in_row]
    else:
        total_value -= values[right_bottom_in_row]

    return total_value
