from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

import re

from adapter import Menu
from adapter import AllowToBuldMenu
from adapter import Timeable
from gui import EditAccount
from core_files import Account

class EditAccountMenu(Menu):   # mit vererbung könnten die __init__, open- close_menu funktionen ausgelassen werden
    def __init__(self, gui: AllowToBuldMenu, timer: Timeable, account: str):
        self.gui = gui
        self.timer = timer
        self.menu_interactables = "list of interactables"

        #problems:
        # einholen der werte von Account
        # speichern der Werte

    def get_account_value():
        pass

    def enter_text(self, text_field):
        self.timer.blocking_wait_milliseconds(800)
        still_tiyping = True
        while still_tiyping:
            action = self.gui.check_events(self.menu_interactables)
            self.gui.set_element_styles()
            self.gui.update_window()
            self.timer.allow_passes_per_second(90)
            if action == "quit":               # kommt man von diesem if wald weg?
                still_tiyping = False
            if re.search("^.$", action):
                text_field["text"]["content"] = text_field["text"]["content"]+action
                continue
            if action == "backspace":
                text_field["text"]["content"] = text_field["text"]["content"][:-1]
                continue
            if action != "no action":
                still_tiyping = False


    def open_menu(self):
        self.gui.set_window_elements(EditAccount.window_elements)
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
                    choose_menu_active = False
                if action == "input_username":
                    self.enter_text(EditAccount.input_username)
                if action == "input_password":
                    self.enter_text(EditAccount.input_password)
                if action == "input_password_repeat":
                    self.enter_text(EditAccount.input_password_repeat)
                if action == "input_age":
                    self.enter_text(EditAccount.input_age)
                if action == "input_admin":
                    self.enter_text(EditAccount.input_admin)
                if action == "save_button":
                    print("save")
                    choose_menu_active = False
                if action == "cancel_button":
                    print("cancel")
                    choose_menu_active = False
            self.timer.allow_passes_per_second(90)
        self.close_menu()

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []