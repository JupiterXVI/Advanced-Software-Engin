"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import AllowToBuldMenu
from core_files import Game
from core_files import Playground

class GameLibraryMenu():
    """
    global variables
    """
    def __init__(self, gui:  AllowToBuldMenu):
        self.gui =  gui    # ggf in eigene Klasse
        self.gamelist = [] #
        self.menu_interactables = []


    """
    functions
    """
    def add_game_to_library(self, new_game): # ggf in eigene Klasse
        self.gamelist.append(new_game)

    # hier könnte man auch noch open/closed-Principle verwenden
    # -> eine Liste mit bilding-functions um das Menu stück für Stück zu bauen
    def open_main_menu(self):
        print("opening main menu...")
        window = self.gui.create_window()
        self.menu_interactables = self.gui.create_window_elements(window)
        #self.gui.set_styles(interactables)
    

    def close_main_menu(self):
        print("closeing main menu...")
        self.gui.terminate_window()

    def run_main_menu(self):
        print("running main menu...")
        main_menu_active = True
        while main_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action == "quit":
                main_menu_active = False
            if action == "start_button":
                print("start")
            if action == "exit_button":
                print("exit")
            if action == "option_button":
                print("option")

            #check_frame_rate()
        self.close_main_menu()




if __name__ == "__main__":
    pass