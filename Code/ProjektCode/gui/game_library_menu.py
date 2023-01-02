"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import Menu
from adapter import AllowToBuldMenu
from adapter import Timeable
from gui import MainMenu


# this class is the zentral menu from which the user can access the games and other options,
# as well as the zentrall data forwareder between games and the playground
class GameLibraryMenu(Menu):
    """
    global variables
    """
    def __init__(self, gui: AllowToBuldMenu, choose_game: Menu, manage_account: Menu, timer: Timeable):
        # objekt of a class which can visualize the menus/games
        self.gui =  gui    # ggf in eigene Klasse
        self.choose_game = choose_game
        self.manage_account = manage_account
        self.timer = timer
        #   
        self.newly_created = True
        # list of interactables on the main menu
        self.menu_interactables = []
        
        # list of game objekts
        self.gamelist = [] # ggf in eigene Klasse
        


    """
    functions
    """
    # this funktion adds a given game objekt to a list of game obekts
    def add_game_to_library(self, new_game): # ggf in eigene Klasse
        self.gamelist.append(new_game)

    # hier könnte man auch noch open/closed-Principle verwenden
    # -> eine Liste mit bilding-functions um das Menu stück für Stück zu bauen
    # this funktion uses the gui objekt to create a menu form the class parameters
    def open_menu(self):
        if self.newly_created:
            print("first time opening main menu...")
            self.gui.set_window_info(MainMenu.window)
            self.gui.set_window_elements(MainMenu.window_elements)
            self.gui.create_window()
            self.newly_created = False
        self.gui.set_window_elements(MainMenu.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()
    
    # this funktion closes the created menu window
    def close_menu(self):
        print("closing main menu...")
        self.gui.terminate_window()

    # this funktion is the loop to run the main menu, checking for user interaktion
    def run_menu(self):
        print("running main menu...")
        main_menu_active = True
        action = "waiting for action"
        while main_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            # print(action)  # Debugging
            if action != "no action":
                if action == "quit":               # kommt man von diesem if wald weg?
                    main_menu_active = False
                if action == "choose_game_button":
                    self.gui.clear_window()
                    self.menu_interactables = []
                    self.choose_game.open_menu()
                    self.choose_game.run_menu()
                    self.open_menu()
                    self.timer.blocking_wait_milliseconds(800)
                if action == "account_button":
                    print("account")
                if action == "exit_button":
                    print("exit")
                    main_menu_active = False
                if action == "circle_button":
                    print("circle")
            self.timer.allow_passes_per_second(90)
        self.close_menu()




if __name__ == "__main__":
    pass