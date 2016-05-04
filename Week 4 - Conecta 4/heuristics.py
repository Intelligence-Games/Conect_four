import random

from connectfour import ConnectFour


class Heuristics:
    def __init__(self):
        self.game = ConnectFour()
        self.values = {
            0: 0,
            1: 100,
            2: 1000,
            3: 10000
        }
        self.board = None

    def random_heuristic(self, state=None):
        return random.randint(-100, 100)

    def best_move_heuristic(self, state=None):
        self.board = state.board
        if state.utility == 1:
            return state.utility * 10000000
        if state.utility == -1:
            return state.utility * 5000000

        result = 0
        for column in range(1, 7):
            for row in range(1, 8):
                if (column, row) in state.moves:
                    result += self.__best_direction(column, row, state=state)
                    break
        return result

    def __best_direction(self, coordinate_x, coordinate_y, state):
        return self.__horizontal(coordinate_x, coordinate_y, state) \
               + self.__vertical(coordinate_x, coordinate_y, state) \
               + self.__diagonal(coordinate_x, coordinate_y, state) \
               + self.__inverse_diagonal(coordinate_x, coordinate_y, state)

    def __calculate_in_row(self, player, coordinate_x, coordinate_y):
        in_row = 0
        if player is not None:
            index = 1
            while index < 4:
                if self.board.get((coordinate_x - index, coordinate_y)) == player:
                    in_row += 1
                else:
                    break
                index += 1
        return in_row

    def __vertical(self, coordinate_x, coordinate_y, state):

        bottom_player = self.board.get((coordinate_x, coordinate_y - 1))
        top_in_row = self.__calculate_in_row(bottom_player, coordinate_x, coordinate_y)

        top_player = self.board.get((coordinate_x, coordinate_y + 1))
        bottom_in_row = self.__calculate_in_row(top_player, coordinate_x, coordinate_y)

        total_value = 0
        if bottom_player == self.game.to_move(state):
            total_value += self.values[bottom_in_row]
        else:
            total_value -= self.values[bottom_in_row]

        if top_player == self.game.to_move(state):
            total_value += self.values[top_in_row]
        else:
            total_value -= self.values[top_in_row]

        return total_value

    def __horizontal(self, coordinate_x, coordinate_y, state):

        left_player = self.board.get((coordinate_x - 1, coordinate_y))
        left_in_row = self.__calculate_in_row(left_player, coordinate_x, coordinate_y)

        right_player = self.board.get((coordinate_x + 1, coordinate_y))
        right_in_row = self.__calculate_in_row(right_player, coordinate_x, coordinate_y)

        total_value = 0
        if left_player == self.game.to_move(state):
            total_value += self.values[left_in_row]
        else:
            total_value -= self.values[left_in_row]

        if right_player == self.game.to_move(state):
            total_value += self.values[right_in_row]
        else:
            total_value -= self.values[right_in_row]

        return total_value

    def __diagonal(self, coordinate_x, coordinate_y, state):

        top_right_player = self.board.get((coordinate_x + 1, coordinate_y + 1))
        top_right_in_row = self.__calculate_in_row(top_right_player, coordinate_x, coordinate_y)

        left_bottom_player = self.board.get((coordinate_x - 1, coordinate_y - 1))
        left_bottom_in_row = self.__calculate_in_row(left_bottom_player, coordinate_x, coordinate_y)

        total_value = 0
        if left_bottom_player == self.game.to_move(state):
            total_value += self.values[left_bottom_in_row]
        else:
            total_value -= self.values[left_bottom_in_row]

        if top_right_player == self.game.to_move(state):
            total_value += self.values[top_right_in_row]
        else:
            total_value -= self.values[top_right_in_row]

        return total_value

    def __inverse_diagonal(self, coordinate_x, coordinate_y, state):

        top_left_player = self.board.get((coordinate_x - 1, coordinate_y + 1))
        top_left_in_row = self.__calculate_in_row(top_left_player, coordinate_x, coordinate_y)

        right_bottom_player = self.board.get((coordinate_x + 1, coordinate_y - 1))
        right_bottom_in_row = self.__calculate_in_row(right_bottom_player, coordinate_x, coordinate_y)

        total_value = 0
        if top_left_player == self.game.to_move(state):
            total_value += self.values[top_left_in_row]
        else:
            total_value -= self.values[top_left_in_row]

        if right_bottom_player == self.game.to_move(state):
            total_value += self.values[right_bottom_in_row]
        else:
            total_value -= self.values[right_bottom_in_row]

        return total_value
