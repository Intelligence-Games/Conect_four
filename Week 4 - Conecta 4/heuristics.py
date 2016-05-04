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
        self.state = None

    def random_heuristic(self, state=None):
        return random.randint(-100, 100)

    def best_move_heuristic(self, state=None):
        self.state = state

        if state.utility == 1:
            return state.utility * 10000000
        if state.utility == -1:
            return state.utility * 5000000

        result = 0
        for column in range(1, 7):
            for row in range(1, 8):
                if (column, row) in state.moves:
                    result += self.__best_direction(column, row)
                    break
        return result

    def __best_direction(self, coordinate_x, coordinate_y):
        return self.__horizontal(coordinate_x, coordinate_y) \
               + self.__vertical(coordinate_x, coordinate_y) \
               + self.__diagonal(coordinate_x, coordinate_y) \
               + self.__inverse_diagonal(coordinate_x, coordinate_y)

    def __vertical(self, coordinate_x, coordinate_y):

        top_player = self.__get_player_at(coordinate_x, coordinate_y + 1)
        top_in_row = self.__calculate_left_in_row(top_player, coordinate_x, coordinate_y)

        bottom_player = self.__get_player_at(coordinate_x, coordinate_y - 1)
        bottom_in_row = self.__calculate_right_in_row(bottom_player, coordinate_x, coordinate_y)

        return self.__get_total_value(top_player, bottom_player, top_in_row, bottom_in_row)

    def __horizontal(self, coordinate_x, coordinate_y):

        left_player = self.__get_player_at(coordinate_x - 1, coordinate_y)
        left_in_row = self.__calculate_left_in_row(left_player, coordinate_x, coordinate_y)

        right_player = self.__get_player_at(coordinate_x + 1, coordinate_y)
        right_in_row = self.__calculate_right_in_row(right_player, coordinate_x, coordinate_y)

        total_value = self.__get_total_value(left_player, right_player, left_in_row, right_in_row)

        return total_value

    def __diagonal(self, coordinate_x, coordinate_y):

        left_bottom_player = self.__get_player_at(coordinate_x - 1, coordinate_y - 1)
        left_bottom_in_row = self.__calculate_left_in_row(left_bottom_player, coordinate_x, coordinate_y)

        top_right_player = self.__get_player_at(coordinate_x + 1, coordinate_y + 1)
        top_right_in_row = self.__calculate_right_in_row(top_right_player, coordinate_x, coordinate_y)

        total_value = self.__get_total_value(left_bottom_player, top_right_player, left_bottom_in_row, top_right_in_row)

        return total_value

    def __inverse_diagonal(self, coordinate_x, coordinate_y):

        top_left_player = self.__get_player_at(coordinate_x - 1, coordinate_y + 1)
        top_left_in_row = self.__calculate_left_in_row(top_left_player, coordinate_x, coordinate_y)

        right_bottom_player = self.__get_player_at(coordinate_x + 1, coordinate_y - 1)
        right_bottom_in_row = self.__calculate_right_in_row(right_bottom_player, coordinate_x, coordinate_y)

        total_value = self.__get_total_value(right_bottom_player, top_left_player, right_bottom_in_row, top_left_in_row)

        return total_value

    def __get_player_at(self, coordinate_x, coordinate_y):
        return self.state.board.get((coordinate_x, coordinate_y))

    def __calculate_left_in_row(self, player, coordinate_x, coordinate_y):
        in_row = 0
        if player is not None:
            index = 1
            while index < 4:
                if self.__get_player_at(coordinate_x - index, coordinate_y) == player:
                    in_row += 1
                else:
                    break
                index += 1
        return in_row

    def __calculate_right_in_row(self, player, coordinate_x, coordinate_y):
        in_row = 0
        if player is not None:
            index = 1
            while index < 4:
                if self.__get_player_at(coordinate_x + index, coordinate_y) == player:
                    in_row += 1
                else:
                    break
                index += 1
        return in_row

    def __get_total_value(self, left_player, right_player, left_in_row, right_in_row):
        total_value = 0
        if right_player == self.game.to_move(self.state):
            total_value += self.values[right_in_row]
        else:
            total_value -= self.values[right_in_row]
        if left_player == self.game.to_move(self.state):
            total_value += self.values[left_in_row]
        else:
            total_value -= self.values[left_in_row]
        return total_value
