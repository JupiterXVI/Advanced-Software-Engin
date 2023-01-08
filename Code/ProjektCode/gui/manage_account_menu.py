"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import Menu
from adapter import AllowToBuldMenu
from adapter import Timeable
from gui import ManageAccount
from gui import EditAccountMenu

class ManageAccountMenu(Menu):
    """
    global variables
    """
    def __init__(self, gui: AllowToBuldMenu, timer: Timeable):
        self.gui = gui
        self.timer = timer
        self.menu_interactables = "list of interactables"
        
    """
    functions
    """
    def open_menu(self):
        self.gui.set_window_elements(ManageAccount.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()

    def edit_account(self, account_index):
        work_on_account = EditAccountMenu(self.gui, self.timer, "account")
        self.gui.clear_window()
        self.menu_interactables = []
        work_on_account.open_menu()
        work_on_account.run_menu()
        self.open_menu()
        self.timer.blocking_wait_milliseconds(800)
    

    def delete_account(self, account_index):
        pass

    def run_menu(self):
        self.timer.blocking_wait_milliseconds(800)
        choose_menu_active = True
        action = "waiting for action"
        while choose_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action != "no action":
                print(action)
                if action == "quit":               # kommt man von diesem if wald weg?
                    choose_menu_active = False      # Sicher auch mit liste möglich
                if action == "account_1_name":
                    self.edit_account(1)
                if action == "account_1_delete":
                    self.delete_account(1)
                if action == "account_2_name":
                    self.edit_account(2)
                if action == "account_2_delete":
                    self.delete_account(2)
                if action == "account_3_name":
                    self.edit_account(3)
                if action == "account_3_delete":
                    self.delete_account(3)
                if action == "account_4_name":
                    self.edit_account(4)
                if action == "account_4_delete":
                    self.delete_account(4)
                if action == "account_5_name":
                    self.edit_account(5)
                if action == "account_5_delete":
                    self.delete_account(5)
                if action == "back_button":
                    print("back")
                    choose_menu_active = False
            self.timer.allow_passes_per_second(90)
        self.close_menu()

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []