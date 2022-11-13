"""
imports
"""
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
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