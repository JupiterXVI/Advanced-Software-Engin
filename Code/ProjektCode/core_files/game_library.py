"""
imports
"""
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from core_files.game import Game
from core_files.playground import Playground

class GameLibrary():
    """
    global variables
    """
    def __init__(self):
        self.gamelist = []

    """
    functions
    """
    def add_game_to_library(self, new_game):
        self.gamelist.append(new_game)

    def open_main_menu(self):
        pass
    