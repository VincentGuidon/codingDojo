# Définir un "solver" pour le solitaire
# En entrée une position, retourne la liste des coups pour avoir le moins de boules restantes ?
# nombre de billes restantes
# https://fr.wikipedia.org/wiki/Solitaire_(casse-t%C3%AAte)
# Partir sur du brut force
# Voir par la suite si on peut faire un arbre de décision
# adapter sur différentes formes de plateau ?
import sys
from typing import Iterable


def determinate_minimum_number_of_marbles_at_the_end(board_string):
    board_array = convert_board_to_array(board_string)
    result = calculate_minimum_number_of_marbles_for_a_board(board_array)
    return result


def calculate_minimum_number_of_marbles_for_a_board(board_array):
    board = Board(board_array).copy()
    solutions_tree = determinate_all_solutions_for_a_board(board)

    if isinstance(solutions_tree, Board):
        minimum_number_of_marbles = retrieve_number_of_marble(board)
    else:
        minimum_number_of_marbles = 666
        # TODO faut récursivé laul
        for solution in solutions_tree:
            marbles_for_this_solution = retrieve_number_of_marble(solution)
            minimum_number_of_marbles = marbles_for_this_solution if marbles_for_this_solution < minimum_number_of_marbles else minimum_number_of_marbles

    return minimum_number_of_marbles


def get_number_of_marbles_for_a_line(board_line):
    return board_line.count('O')


def retrieve_number_of_marble(board):
    if not isinstance(board, Board):
        return 666
    result_per_solution = 0
    for line in board.lines:
        result_per_solution += line.count('O')
    return result_per_solution


def convert_board_to_array(position_lines):
    position_lines = position_lines.replace(" ", "")
    return [line for line in position_lines.split("\n") if line != ""]


def determinate_all_solutions_for_a_line(board, index):
    result = []
    if is_eatable_to_the_right(board.lines[index]):
        board_copy = board.copy()
        board_copy.eat_to_the_right(index)
        result.append(determinate_all_solutions_for_a_line(board_copy, index))
    if is_eatable_to_the_left(board.lines[index]):
        board_copy = board.copy()
        board_copy.eat_to_the_left(index)
        result.append(determinate_all_solutions_for_a_line(board_copy, index))
    return board if len(result) == 0 else result


def determinate_all_solutions_for_a_board(board):
    result = []
    board_rotate = board.rotate()
    board_copy = board.copy()
    for i in range(len(board_copy.lines)):
        if is_eatable_to_the_right(board_copy.lines[i]):
            result.append(determinate_all_solutions_for_a_line(board_copy, i))
        if is_eatable_to_the_left(board_copy.lines[i]):
            result.append(determinate_all_solutions_for_a_line(board_copy, i))

    for i in range(len(board_rotate.lines)):
        if is_eatable_to_the_right(board_rotate.lines[i]):
            result.append(determinate_all_solutions_for_a_line(board_rotate, i))
        if is_eatable_to_the_left(board_rotate.lines[i]):
            result.append(determinate_all_solutions_for_a_line(board_rotate, i))

    if len(result) == 0:
        return board
    return result


def is_eatable_to_the_left(board_line):
    return "XOO" in board_line


def is_eatable_to_the_right(board_line):
    return "OOX" in board_line


def is_eatable_up(board, column_index):
    line = board.get_column(column_index)
    return is_eatable_to_the_left(line)


def is_eatable_down(board, column_index):
    line = board.get_column(column_index)
    return is_eatable_to_the_right(line)


class Board:
    def __init__(self, array_lines):
        self.lines = array_lines.copy()

    def get_column(self, index):
        return ''.join([line[index] for line in self.lines])

    def rotate(self):
        return Board([self.get_column(col) for col in range(len(self.lines[0]))])

    def copy(self):
        return Board(self.lines)

    def eat_to_the_right(self, index):
        self.lines[index] = self.lines[index].replace("OOX", "XXO", 1)

    def eat_to_the_left(self, index):
        self.lines[index] = self.lines[index].replace("XOO", "OXX", 1)
