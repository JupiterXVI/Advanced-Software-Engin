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
from core_files import AccountList

class ManageAccountMenu(Menu):
    """
    global variables
    """
    def __init__(self, gui: AllowToBuldMenu, timer: Timeable, account_list: AccountList):
        self.gui = gui
        self.timer = timer
        self.menu_interactables = "list of interactables"
        self.account_list = account_list

    # TODO
    # add new account
    # delete account
        
    """
    functions
    """
    def open_menu(self):
        self.gui.set_window_elements(ManageAccount.window_elements)
        self.menu_interactables = self.gui.create_window_interaction_elements()
        self.gui.set_element_styles()


    def get_account_list_on_screan(self): # kake, aber in einer liste hat es nicht funktionert
        try:
            ManageAccount.account_1_name["text"]["content"] = self.account_list.account[3].get_name()
        except:
            print("No Account in Slot 1")
        try:
            ManageAccount.account_2_name["text"]["content"] = self.account_list.account[4].get_name()
        except:
            print("No Account in Slot 2")
        try:
            ManageAccount.account_3_name["text"]["content"] = self.account_list.account[5].get_name()
        except:
            print("No Account in Slot 3")
        try:
            ManageAccount.account_4_name["text"]["content"] = self.account_list.account[6].get_name()
        except:
            print("No Account in Slot 4")
        try:
            ManageAccount.account_5_name["text"]["content"] = self.account_list.account[7].get_name()
        except:
            print("No Account in Slot 5")


    def edit_account(self, account_index):
        anonyme_user_count = 2
        work_on_account = EditAccountMenu(self.gui, self.timer, self.account_list.account[account_index+anonyme_user_count])
        self.gui.clear_window()
        self.menu_interactables = []
        work_on_account.open_menu()
        work_on_account.run_menu()
        self.open_menu()
        self.timer.blocking_wait_milliseconds(800)
    

    def delete_account(self, account_index):
        pass


    def run_menu(self):
        self.get_account_list_on_screan()
        self.gui.set_element_styles()
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