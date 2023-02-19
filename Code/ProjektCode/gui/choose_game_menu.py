from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from time import sleep

from adapter import Menu
from adapter import AllowToBuldMenu
from gui import ChooseGame

class ChooseGameMenu(Menu):
    def __init__(self, gui: AllowToBuldMenu):
        self.gui = gui
        self.menu_interactables = "list of interactables"


    def open_menu(self):
        self.gui.set_window_elements(ChooseGame.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()
        self.gui.update_window()
        

    def run_menu(self):
        sleep(Menu.blocking_wait_seconds)
        choose_menu_active = True
        action = "waiting for action"
        while choose_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action != "no action":
                if action == "quit":               # kommt man von diesem if wald weg?
                    self.gui.terminate_window()
                if action == "space_invaders_button":
                    print("Space Invaders")
                if action == "tic_tac_toe_button":
                    print("Tic Tac Toe")
                if action == "back_button":
                    print("back")
                    choose_menu_active = False
            sleep(Menu.allow_passes_per_second)
        self.close_menu()

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []