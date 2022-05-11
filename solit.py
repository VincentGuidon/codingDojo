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
    # result_rotated = calculate_minimum_number_of_marbles_for_a_board(rotate_board_array(board_array))
    result = calculate_minimum_number_of_marbles_for_a_board(board_array)
    # return min(result, result_rotated)
    return result

def rotate_board_array(board_array):
    return [transform_column_to_line(board_array, col) for col in range(len(board_array[0]))]


def calculate_minimum_number_of_marbles_for_a_board(board_array):
    # return sum([calculate_minimum_number_of_marbles_for_a_line(line, board_array) for line in board_array])
    # for line in board_array:
    #     solutions_map = determinate_all_solutions_for_a_line(line)
        # solutions_list = flatten(solutions_map)
        # minimum_number_of_marbles = retrieve_minimal_number_of_marble(solutions_list, get_number_of_marbles_for_a_line(line))
        # return minimum_number_of_marbles
    # for line in rotate_board_array(board_array):
    solutions_map = determinate_all_solutions_for_a_board(board_array)
    solutions_list = flatten(solutions_map)

    minimum_number_of_marbles = retrieve_minimal_number_of_marble(solutions_list)
    return minimum_number_of_marbles

# def calculate_minimum_number_of_marbles_for_a_line(line, board_array):
#     solutions_map = determinate_all_solutions_for_a_line(line)
#     solutions_list = flatten(solutions_map)
#     minimum_number_of_marbles = retrieve_minimal_number_of_marble(solutions_list, get_number_of_marbles_for_a_line(line))
#     return minimum_number_of_marbles


def get_number_of_marbles_for_a_line(board_line):
    return board_line.count('O')


def retrieve_minimal_number_of_marble(solutions):
    result = 9000
    for solution in solutions:
        result_per_solution = 0
        for line in solution:
            result_per_solution += line.count('O')
        if (result > result_per_solution):
            result = result_per_solution
    # return min([solution.count('O') for solution in solutions])
    return result

# def retrieve_minimal_number_of_marble(solutions, min_result):
#     for solution in solutions:
#         solution_count = solution.count('O')
#         min_result = solution_count if solution_count < min_result else min_result
#     return min_result


def flatten(items):
    if type(items) == str:
        return
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


def convert_board_to_array(position_lines):
    position_lines = position_lines.replace(" ", "")
    return [line for line in position_lines.split("\n") if line != ""]


def determinate_all_solutions_for_a_line(board_line):
    result = []
    if is_eatable_to_the_right(board_line):
        result.append(determinate_all_solutions_for_a_line(board_line.replace("OOX", "XXO")))
    if is_eatable_to_the_left(board_line):
        result.append(determinate_all_solutions_for_a_line(board_line.replace("XOO", "OXX")))
    return board_line if len(result) == 0 else result


# TODO IL FAUT APPEND LE NOUVEAU BOARD ARRAY AU LIEU DE LA LIGNE MODIFIEE. C'EST LE PARAMETRE DE determinate_all_solutions_for_a_line qu'il faut modifier pour transmettre le nouveau tableau
def determinate_all_solutions_for_a_board(board_array):
    result = []
    board_rotate = rotate_board_array(board_array)
    for board_line in board_array:
        if is_eatable_to_the_right(board_line):
            result.append(determinate_all_solutions_for_a_line(board_line.replace("OOX", "XXO")))
        if is_eatable_to_the_left(board_line):
            result.append(determinate_all_solutions_for_a_line(board_line.replace("XOO", "OXX")))
    for board_line_rotate in board_rotate:
        if is_eatable_to_the_right(board_line_rotate):
            result.append(determinate_all_solutions_for_a_line(board_line_rotate.replace("OOX", "XXO")))
        if is_eatable_to_the_left(board_line_rotate):
            result.append(determinate_all_solutions_for_a_line(board_line_rotate.replace("XOO", "OXX")))

    if len(result) == 0:
        result.append(board_array)
    return result
    # return board_array if len(result) == 0 else result


def is_eatable_to_the_left(board_line):
    return "XOO" in board_line


def is_eatable_to_the_right(board_line):
    return "OOX" in board_line


def is_eatable_up(board_array, column_index):
    line = transform_column_to_line(board_array, column_index)
    return is_eatable_to_the_left(line)


def transform_column_to_line(board_array, column_index):
    return ''.join([table_line[column_index] for table_line in board_array])


def is_eatable_down(board_array, column_index):
    line = transform_column_to_line(board_array, column_index)
    return is_eatable_to_the_right(line)
