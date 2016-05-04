import random
from connectfour import ConnectFour

game = ConnectFour()


def random_heuristic(state=None):
    return random.randint(-100, 100)


def best_move_heuristic(state):
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
    return horizontal(tuple, state)


values = {
    0: 0,
    1: 100,
    2: 1000,
    3: 10000
}


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
            if state.board.get((tuple[0] + index, tuple[1])) == game.to_move(state):
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
