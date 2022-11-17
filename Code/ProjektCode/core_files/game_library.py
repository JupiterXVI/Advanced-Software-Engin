"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
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

    # hier könnte man auch noch open/closed-Principle verwenden
    # -> eine Liste mit bilding-functions um das Menu stück für Stück zu bauen
    def open_main_menu(self):
        print("opening main menu...")
        window = self.gui.create_window()
        #self.gui.create_buttons()
        #self.gui.set_styles()
        



if __name__ == "__main__":
    pass