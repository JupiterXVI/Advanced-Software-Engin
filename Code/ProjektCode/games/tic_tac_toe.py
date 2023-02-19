"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.game import Game
from games.graphics import ChooseGraphicTTT



class TicTacToe(Game):
    """
    global variables
    """
    def __init__(self):
        super().__init__(
            game_id = 1, 
            name = "TicTacToe", 
            player_count = 2, 
            game_elements = ChooseGraphicTTT.game_elements
            )

    """
    functions
    """
    def start(self):
        print("\nStart TicTacTo\n")
        