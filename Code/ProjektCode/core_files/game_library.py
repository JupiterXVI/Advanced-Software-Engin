"""
imports
"""
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from adapter import AllowToBuldMenu
from core_files import Game
from core_files import Playground

class GameLibrary():
    """
    global variables
    """
    def __init__(self, gui:  AllowToBuldMenu):
        self.gui =  gui
        self.gamelist = []

    """
    functions
    """
    def add_game_to_library(self, new_game):
        self.gamelist.append(new_game)

    def open_main_menu(self):
        print("opening main menu...")
        window = self.gui.create_window()
        #self.gui.create_buttons()
        #self.gui.set_styles()
        



if __name__ == "__main__":
    pass