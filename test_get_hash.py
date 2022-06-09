from unittest import TestCase

from solit import Board, convert_board_to_array


# - = vide
# X = trous
# O = billes
# from solitaire.solit import determinate_minimum_number_of_marbles_at_the_end

class Test(TestCase):
    def test_hash_one_rotation(self):
        tab_not_rotated = Board(convert_board_to_array("""
            XOOX
            OXXX
            OOXO
            XOOO"""))
        tab_rotated_one_fourth = Board(convert_board_to_array("""
            XOOX
            OOXO
            OXXO
            OOXX
            """))
        self.assertEqual(tab_not_rotated.get_hash(), tab_rotated_one_fourth.get_hash())

    def test_hash_two_rotations(self):
        tab_not_rotated = Board(convert_board_to_array("""
            XOOX
            OXXX
            OOXO
            XOOO"""))
        tab_rotated_two_fourths = Board(convert_board_to_array("""
            OOOX
            OXOO
            XXXO
            XOOX
            """))
        self.assertEqual(tab_not_rotated.get_hash(), tab_rotated_two_fourths.get_hash())

    def test_hash_differents(self):
        tab_not_rotated = Board(convert_board_to_array("""
            XOOX
            OXXX
            OOXO
            XOOO"""))
        tab_rotated_two_fourths = Board(convert_board_to_array("""
            OOOX
            OXXO
            XXXO
            XOOX
            """))
        self.assertNotEqual(tab_not_rotated.get_hash(), tab_rotated_two_fourths.get_hash())

    def test_hash_vertical_mirror(self):
        tab = Board(convert_board_to_array("""
        --X--
        -OXX-
        XXOOX
        -XXO-
        --X--
        """))
        tab_mirror = Board(convert_board_to_array("""
        --X--
        -OXX-
        XXOXX
        -XOO-
        --X--
        """))
        self.assertEqual(tab.get_hash(), tab_mirror.get_hash())


    def test_hash_horizontal_mirror(self):
        tab = Board(convert_board_to_array("""
        --X--
        -OOO-
        XXOOO
        -OXO-
        --O--
        """))
        tab_mirror = Board(convert_board_to_array("""
        --O--
        -OXO-
        XXOOO
        -OOO-
        --X--
        """))
        self.assertEqual(tab.get_hash(), tab_mirror.get_hash())

    def test_vertical_mirror(self):
        tab = Board(convert_board_to_array("""
        --X--
        -OXX-
        XXOOX
        -XXO-
        --X--
        """))
        tab_mirror = Board(convert_board_to_array("""
        --X--
        -XXO-
        XOOXX
        -OXX-
        --X--
        """))
        self.assertEqual(tab.mirror().lines, tab_mirror.lines)
