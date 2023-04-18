"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

import unittest
from games import TicTacToe

import coverage
cov = coverage.Coverage()
cov.start()

class test_TicTacToe(unittest.TestCase):

    def test_change_symbols(self):
        self.game = TicTacToe()
        self.game.active_player = 'O'
        self.game.change_symbols()
        self.assertEqual(self.game.active_player, 'X')
        self.game.change_symbols()
        self.assertEqual(self.game.active_player, 'O')
            
if __name__ == '__main__':
    unittest.main()

cov.stop()
cov.save()
cov.report()