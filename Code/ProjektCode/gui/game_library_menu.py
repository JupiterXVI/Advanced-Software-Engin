"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import AllowToBuldMenu
from adapter import Timeable
from core_files import Game
from core_files import Playground

# this class is the zentral menu from which the user can access the games and other options,
# as well as the zentrall data forwareder between games and the playground
class GameLibraryMenu():
    """
    global variables
    """
    def __init__(self, gui:  AllowToBuldMenu):
        # objekt of a class which can visualize the menus/games
        self.gui =  gui    # ggf in eigene Klasse
        # list of game objekts
        self.gamelist = [] # ggf in eigene Klasse
        # list of interactables on the main menu
        self.menu_interactables = []


    """
    functions
    """
    # this funktion adds a given game objekt to a list of game obekts
    def add_game_to_library(self, new_game): # ggf in eigene Klasse
        self.gamelist.append(new_game)

    # hier könnte man auch noch open/closed-Principle verwenden
    # -> eine Liste mit bilding-functions um das Menu stück für Stück zu bauen
    # this funktion uses the gui objekt to create a menu form the class parameters
    def open_main_menu(self):
        print("opening main menu...")
        window = self.gui.create_window()
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles(window)
    
    # this funktion closes the created menu window
    def close_main_menu(self):
        print("closing main menu...")
        self.gui.terminate_window()

    # this funktion is the loop to run the main menu, checking for user interaktion
    def run_main_menu(self, frame_checker: Timeable):
        print("running main menu...")
        main_menu_active = True
        while main_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action == "quit":               # kommt man von diesem if wald weg?
                main_menu_active = False
            if action == "start_button":
                print("start")
            if action == "exit_button":
                print("exit")
            if action == "option_button":
                print("option")
            if action == "circle_button":
                print("circle")

            frame_checker.allow_passes_per_second(60)
        self.close_main_menu()




if __name__ == "__main__":
    pass