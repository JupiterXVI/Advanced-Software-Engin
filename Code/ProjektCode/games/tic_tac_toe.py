"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.game import Game



class TicTacToe(Game):
    """
    global variables
    """
    def __init__(self, game_id, name, player_count):
        super().__init__(game_id, name, player_count)

    """
    functions
    """