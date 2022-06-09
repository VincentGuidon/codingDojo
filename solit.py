# Définir un "solver" pour le solitaire
# En entrée une position, retourne la liste des coups pour avoir le moins de boules restantes ?
# nombre de billes restantes
# https://fr.wikipedia.org/wiki/Solitaire_(casse-t%C3%AAte)
# Partir sur du brut force
# Voir par la suite si on peut faire un arbre de décision
# adapter sur différentes formes de plateau ?

# TODO Miroir
import itertools

counter = itertools.count()


def determinate_minimum_number_of_marbles_at_the_end(board_string):
    board_array = convert_board_to_array(board_string)
    result = calculate_minimum_number_of_marbles_for_a_board(board_array)
    return result


def calculate_minimum_number_of_marbles_for_a_board(board_array):
    board = Board(board_array)
    hash_set = set()
    solutions_tree = determinate_all_solutions_for_a_board(board, hash_set)
    return retrieve_number_of_marble(solutions_tree)


def get_number_of_marbles_for_a_line(board_line):
    return board_line.count('O')


def retrieve_number_of_marble(boards):
    if isinstance(boards, Board):
        result = boards.count()

    else:
        result = float('inf')
        for solution in boards:
            tmp_result = retrieve_number_of_marble(solution)
            result = tmp_result if tmp_result < result else result

    return result


def convert_board_to_array(position_lines):
    position_lines = position_lines.replace(" ", "")
    return [line for line in position_lines.split("\n") if line != ""]


def determinate_all_solutions_for_a_board(board, hash_list):
    board.print()
    result = []
    if board.get_hash() in hash_list:
        return board
    hash_list.add(board.get_hash())
    iterate_on_line(board, hash_list, result)
    iterate_on_line(board.rotate(), hash_list, result)
    if len(result) == 0:
        return board
    return result


def iterate_on_line(board, hash_list, result):
    for i in range(len(board.lines)):
        # TODO CSA
        if is_eatable_to_the_right(board.lines[i]):
            board_copy = board.copy()
            board_copy.eat_to_the_right(i)
            result.append(determinate_all_solutions_for_a_board(board_copy, hash_list))
        if is_eatable_to_the_left(board.lines[i]):
            board_copy = board.copy()
            board_copy.eat_to_the_left(i)
            result.append(determinate_all_solutions_for_a_board(board_copy, hash_list))


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
        return Board([self.get_column(col) for col in reversed(range(len(self.lines[0])))])

    def mirror(self):
        result = []
        for line in self.lines :
            result.append(line[::-1])
        return Board(result)


    def copy(self):
        return Board(self.lines)

    def eat_to_the_right(self, index):
        self.lines[index] = self.lines[index].replace("OOX", "XXO", 1)

    def eat_to_the_right_with_copy(self, index):
        copy = self.copy()
        copy.lines[index] = copy.lines[index].replace("OOX", "XXO", 1)
        return copy

    def eat_to_the_left(self, index):
        self.lines[index] = self.lines[index].replace("XOO", "OXX", 1)

    def print(self):
        print(next(counter), self.lines, self.count())

    def count(self):
        result = 0
        for line in self.lines:
            result += line.count('O')
        return result

    def not_equals(self, board_to_compare):
        for index in range(len(board_to_compare.lines)):
            if (board_to_compare.lines[index] != self.lines[index]):
                return True
        return False

    def get_hash(self):
        self_rotated_once = self.rotate()
        self_rotated_twice = self_rotated_once.rotate()
        self_mirrored = self.mirror()
        self_mirrored_rotated_once = self_mirrored.rotate()
        self_mirrored_rotated_twice = self_mirrored_rotated_once.rotate()
        self_mirrored_rotated_thrice = self_mirrored_rotated_twice.rotate()

        return hash(tuple(self.lines)) \
               + hash(tuple(self_rotated_once.lines)) \
               + hash(tuple(self_rotated_twice.lines)) \
               + hash(tuple(self_rotated_twice.rotate().lines)) \
               + hash(tuple(self_mirrored.lines)) \
               + hash(tuple(self_mirrored_rotated_once.lines)) \
               + hash(tuple(self_mirrored_rotated_twice.lines)) \
               + hash(tuple(self_mirrored_rotated_thrice.lines))

