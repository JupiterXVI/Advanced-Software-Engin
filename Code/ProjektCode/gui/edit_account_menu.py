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
    def __init__(self, gui: AllowToBuldMenu, timer: Timeable, account: Account):
        self.gui = gui
        self.timer = timer
        self.menu_interactables = "list of interactables"
        self.account = account
        self.save_changes = False

        #TODO:
        #- markiere welches Feld beschrieben wird

    def get_account_values_on_screen(self):
        EditAccount.input_username["text"]["content"] = str(self.account.get_name())
        EditAccount.input_password["text"]["content"] =  str(self.account.get_password())
        EditAccount.input_password_repeat["text"]["content"] =  str("")
        EditAccount.input_age["text"]["content"] =  str(self.account.get_age())
        EditAccount.input_admin["text"]["content"] =  str(self.account.get_admin())

    def pass_canges_to_account(self):
        self.account.set_name(EditAccount.input_username["text"]["content"])
        self.account.set_password(EditAccount.input_password["text"]["content"])
        self.account.set_age(EditAccount.input_age["text"]["content"])
        if EditAccount.input_admin["text"]["content"] in ["True", "true", "T", "t", "1"]:
            self.account.set_admin(True)
        else:
            self.account.set_admin(False)

    def text_fiel_active(self, active, text_field):
        if active:
            for color_index in range(3):
                text_field["color"][color_index] += 30
        else:
            for color_index in range(3):
                text_field["color"][color_index] -= 30

    def enter_text(self, text_field):
        self.text_fiel_active(True, text_field)
        self.timer.blocking_wait_milliseconds(800)
        still_tiyping = True
        while still_tiyping:
            action = self.gui.check_events(self.menu_interactables)
            self.gui.set_element_styles()
            self.gui.update_window()
            self.timer.allow_passes_per_second(90)
            if action == "quit":               # kommt man von diesem if wald weg?
                self.gui.terminate_window()
            if re.search("^.$", action):
                text_field["text"]["content"] = text_field["text"]["content"]+action
                continue
            if action == "backspace":
                text_field["text"]["content"] = text_field["text"]["content"][:-1]
                continue
            if action != "no action":
                still_tiyping = False
        self.text_fiel_active(False, text_field)

    def check_valid_change(self):
        if EditAccount.input_password["text"]["content"] == EditAccount.input_password_repeat["text"]["content"] and EditAccount.input_username["text"]["content"] != str(""):
            return True
        return False


    def open_menu(self):
        self.gui.set_window_elements(EditAccount.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()
        

    def run_menu(self):
        self.get_account_values_on_screen()
        self.gui.set_element_styles()
        self.timer.blocking_wait_milliseconds(800)
        editing = True
        action = "waiting for action"
        while editing:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action != "no action":
                if action == "quit":               # kommt man von diesem if wald weg?
                    self.gui.terminate_window()
                if action == "input_username":
                    self.enter_text(EditAccount.input_username)
                if action == "input_password":
                    self.enter_text(EditAccount.input_password)
                if action == "input_password_repeat":
                    self.enter_text(EditAccount.input_password_repeat)
                if action == "input_age":
                    self.enter_text(EditAccount.input_age)
                if action == "input_admin":
                    # self.enter_text(EditAccount.input_admin)
                    pass
                if action == "save_button":
                    if self.check_valid_change():
                        print("save")
                        self.pass_canges_to_account()
                        self.save_changes = True
                        editing = False
                if action == "cancel_button":
                    print("cancel")
                    editing = False
            self.timer.allow_passes_per_second(90)
        self.close_menu()

    def has_been_changed(self):
        return self.save_changes

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []