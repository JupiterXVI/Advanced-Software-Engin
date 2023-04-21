"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))


import unittest
from games import TicTacToe


class test_TicTacToe(unittest.TestCase):

    def test_change_symbols(self):
        # arrange
        self.game = TicTacToe()
        self.game.active_player = 'O'

        # act
        self.game.change_symbols()

        # assert
        self.assertEqual(self.game.active_player, 'X')

        # act
        self.game.change_symbols()

        # assert
        self.assertEqual(self.game.active_player, 'O')
            