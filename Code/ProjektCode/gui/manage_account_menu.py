"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from time import sleep

from adapter import Menu
from adapter import GuiBuilder
from gui import ManageAccount
from gui import EditAccountMenu
from core_files import AccountList

from communication import Sender, Reseiver

class ManageAccountMenu(Menu):
    """
    global variables
    """
    def __init__(self):
        # self.gui = gui #gebraucht?
        self.menu_interactables = "list of interactables"
        self.account_list = "not Set"
        self.anonyme_user_count = 2

        self.sender = Sender()
        self.reseiver = Reseiver()

        
    """
    functions
    """
    def change_menu(self):
        #self.get_account_list_on_screan()
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':ManageAccount.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})
        #self.sender.send(category='gui', name='update', info={'function':GuiBuilder.update_window.__name__, 'parameter':''})


    def get_button_from_position(self, position):
        pass

    def run(self):
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    print(message)
                elif message['category'] == "exit":
                    self.sender.send(category='menu', name='exit menus', info={'function':'exit_event', 'parameter':"exit"})
                    menu_in_use = False
                    print("closing menu thread")


    def get_account_list_on_screan(self): # kake, aber in einer liste hat es nicht funktionert
        try:
            ManageAccount.account_1_name["text"]["content"] = self.account_list.account[1+self.anonyme_user_count].get_name()
        except:
            ManageAccount.account_1_name["text"]["content"] = "+"
        try:
            ManageAccount.account_2_name["text"]["content"] = self.account_list.account[2+self.anonyme_user_count].get_name()
        except:
            ManageAccount.account_2_name["text"]["content"] = "+"
        try:
            ManageAccount.account_3_name["text"]["content"] = self.account_list.account[3+self.anonyme_user_count].get_name()
        except:
            ManageAccount.account_3_name["text"]["content"] = "+"
        try:
            ManageAccount.account_4_name["text"]["content"] = self.account_list.account[4+self.anonyme_user_count].get_name()
        except:
            ManageAccount.account_4_name["text"]["content"] = "+"
        try:
            ManageAccount.account_5_name["text"]["content"] = self.account_list.account[5+self.anonyme_user_count].get_name()
        except:
            ManageAccount.account_5_name["text"]["content"] = "+"


    def edit_account(self, account_index):
        if account_index < len(self.account_list.account):
            print(len(self.account_list.account))
            edit_account = account_index
        else:
            self.account_list.add_account("", "", "", False)
            print(len(self.account_list.account))
            edit_account = len(self.account_list.account)-1
        work_on_account = EditAccountMenu(self.gui, self.account_list.account[edit_account])
        self.gui.clear_window()
        self.menu_interactables = []
        work_on_account.open_menu()
        work_on_account.run_menu()
        if work_on_account.has_been_changed():
            self.account_list.save_account_data(self.account_list.account[edit_account])
        elif self.account_list.account[edit_account].get_name() == str(""):
            self.account_list.delete_account(edit_account)
        self.open_menu()
        sleep(Menu.blocking_wait_seconds)
    

    def delete_account(self, account_index):
        if account_index < len(self.account_list.account):
            self.account_list.delete_account(account_index)
        

    def run_menu(self):
        sleep(Menu.blocking_wait_seconds)
        choose_menu_active = True
        action = "waiting for action"
        while choose_menu_active:
            self.get_account_list_on_screan()
            self.gui.set_element_styles()
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action != "no action":
                if action == "quit":               
                    self.gui.terminate_window()      
                if action == "account_1_name":
                    self.edit_account(1+self.anonyme_user_count)
                if action == "account_1_delete":
                    self.delete_account(1+self.anonyme_user_count)
                if action == "account_2_name":
                    self.edit_account(2+self.anonyme_user_count)
                if action == "account_2_delete":
                    self.delete_account(2+self.anonyme_user_count)
                if action == "account_3_name":
                    self.edit_account(3+self.anonyme_user_count)
                if action == "account_3_delete":
                    self.delete_account(3+self.anonyme_user_count)
                if action == "account_4_name":
                    self.edit_account(4+self.anonyme_user_count)
                if action == "account_4_delete":
                    self.delete_account(4+self.anonyme_user_count)
                if action == "account_5_name":
                    self.edit_account(5+self.anonyme_user_count)
                if action == "account_5_delete":
                    self.delete_account(5+self.anonyme_user_count)
                if action == "back_button":
                    print("back")
                    choose_menu_active = False
            sleep(Menu.allow_passes_per_second)
        self.close_menu()


    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []
