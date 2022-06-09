from unittest import TestCase

from solit import determinate_minimum_number_of_marbles_at_the_end


# - = vide
# X = trous
# O = billes
# from solitaire.solit import determinate_minimum_number_of_marbles_at_the_end

class Test(TestCase):
    def test_cas_partiellement_complet_5x5(self):
        position_lines = """
            --O--
            -OOO-
            OOXOO
            -OOO-
            --O--
            """
        self.assertEqual(6, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    # 5937 itérations en 1.72s
    def test_cas_partiellement_complet_5x5_2_complexe(self):
        position_lines = """
            -OOO-
            OOXOO
            OXXXO
            OOXOO
            -OOO-
            """
        self.assertEqual(4, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_cas_partiellement_complet_5x5_2(self):
        position_lines = """
            -OOO-
            OOOOO
            OOXOO
            OOOOO
            -OOO-
            """
        self.assertEqual(4, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_solution_finale(self):
        position_lines = """
            --OOO--
            --OOO--
            OOOOOOO
            OOOXOOO
            OOOOOOO
            --OOO--
            --OOO--
            """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))
