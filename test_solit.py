from unittest import TestCase

from solit import convert_board_to_array, determinate_minimum_number_of_marbles_at_the_end, Board


# - = vide
# X = trous
# O = billes
# from solitaire.solit import determinate_minimum_number_of_marbles_at_the_end


class Test(TestCase):
    def test_avec_une_bille_une_case(self):
        position_lines = """
        O
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_deux_billes_vers_la_droite(self):
        position_lines = """
        OOX
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_deux_billes_vers_la_gauche(self):
        position_lines = """
        XOO
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_deux_billes_sans_trou(self):
        position_lines = """
        OO
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_trois_billes_sans_trou(self):
        position_lines = """
        OOO
        """
        self.assertEqual(3, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_deux_billes_avec_trou_central(self):
        position_lines = """
        OXO
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_avec_deux_sauts(self):
        position_lines = """
        OOXOX
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_quatre_billes_avec_deux_sauts(self):
        position_lines = """
        OOXOXXO
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_quatre_billes_avec_trois_sauts(self):
        position_lines = """
        OOXOXO
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_quatre_billes_avec_trois_sauts_dans_sens_oppose(self):
        position_lines = """
        OOXXOOX
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_six_billes_avec_trois_sauts_dans_sens_oppose(self):
        position_lines = """
        OOXXOOXOO
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_six_billes_avec_deux_sauts_dans_sens_oppose(self):
        position_lines = """
        OOXXOOXOOXOOXX
        """
        self.assertEqual(3, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_deux_billes_sur_chaque_deux_lignes(self):
        position_lines = """
        OOX
        OOX
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_six_billes_sur_chaque_deux_lignes(self):
        position_lines = """
        OOXXOOXOOXOOXX
        OOXXOOXOOXOOXX
        """
        self.assertEqual(6, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_deux_billes_sur_une_colonne_sens_bas(self):
        position_lines = """
        O
        O
        X
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_sur_une_colonne_sens_bas_puis_haut_en_deux_coups(self):
        position_lines = """
        O
        O
        X
        O
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_sur_une_colonne_sens_faut_puis_bas_en_deux_coup(self):
        position_lines = """
        O
        X
        O
        O
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_sur_une_colonne_sens_bas_en_un_coup(self):
        position_lines = """
        O
        O
        X
        X
        O
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_cinq_billes_sur_une_colonne(self):
        position_lines = """
        O
        O
        X
        O
        O
        X
        O
        """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_deux_billes_sur_une_colonne_sens_haut(self):
        position_lines = """
         X
         O
         O
         """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_deux_billes_sur_une_colonne_sens_haut_aucun_coup(self):
        position_lines = """
         O
         X
         O
         """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_quatre_billes_sur_deux_colonnes_avec_une_mangeation(self):
        position_lines = """
         OX
         XO
         OO
         """
        self.assertEqual(3, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_quatre_billes_sur_deux_colonnes_avec_deux_mangeations(self):
        position_lines = """
         OO
         OO
         XX
         """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_six_billes_sur_deux_colonnes_avec_trois_mangeations(self):
        position_lines = """
         OO
         OO
         XX
         XO
         OX
         """
        self.assertEqual(3, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_sur_trois_colonnes_avec_trois_mangeations(self):
        position_lines = """
         OXO
         OXX
         XXO
         """
        self.assertEqual(3, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_trois_billes_en_deux_dimensions_avec_deux_mangeations(self):
        position_lines = """
         OXX
         OXX
         XOX
         """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_une_bille_un_carre(self):
        position_lines = """
        XXX
        XOX
        XXX
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_priorite_gauche(self):
        position_lines = """
        OXOOOOX
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_priorite_droite(self):
        position_lines = """
        XOOOOXO
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_priorite_bas(self):
        position_lines = """
        X
        O
        O
        O
        O
        X
        O
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_priorite_haut(self):
        position_lines = """
        O
        O
        O
        O
        X
        O
        X
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_cas_complexe_4_x_4(self):
        position_lines = """
        XOOX
        OXXX
        OOXO
        XOOO
        """
        self.assertEqual(1, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_vide(self):
        position_lines = """
        OOO--
        --X--
        --OOO
        """
        self.assertEqual(6, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_avec_vide_un_mangeation(self):
        position_lines = """
        OOO--
        --O--
        --XOO
        """
        self.assertEqual(4, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_cas_partiellement_complet_3x3(self):
        position_lines = """
        OOO
        OXO
        OOO
        """
        self.assertEqual(8, determinate_minimum_number_of_marbles_at_the_end(position_lines))

    def test_priorite_mangeation(self):
        position_lines = """
            XOOX
            XOOX
            OXXX
            """
        self.assertEqual(2, determinate_minimum_number_of_marbles_at_the_end(position_lines))