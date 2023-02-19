from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from adapter import Menu
from adapter import AllowToBuldMenu
from adapter import Timeable
from gui import ChooseGame

class ChooseGameMenu(Menu):   # mit vererbung könnten die __init__, open- close_menu funktionen ausgelassen werden
    def __init__(self, gui: AllowToBuldMenu, timer: Timeable):
        self.gui = gui
        self.timer = timer
        self.menu_interactables = "list of interactables"


    def open_menu(self):
        self.gui.set_window_elements(ChooseGame.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()
        

    def run_menu(self):
        self.timer.blocking_wait_milliseconds(800)
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
            self.timer.allow_passes_per_second(90)
        self.close_menu()

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []