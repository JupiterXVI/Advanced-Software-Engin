"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from adapter import Menu
from adapter import GuiBuilder
from gui import ManageAccount
from communication import Sender, Reseiver
from re import search, findall

from gui import EditAccountMenu
from time import sleep

ANONYE_USERS = 2

class ManageAccountMenu(Menu):
    """
    global variables
    """
    def __init__(self):
        # self.gui = gui #gebraucht?
        self.menu_interactables = "list of interactables"
        self.account_list = "not Set"

        self.sender = Sender()
        self.reseiver = Reseiver()

        
    """
    functions
    """
    def change_menu(self):
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':ManageAccount.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})
        #self.get_account_list_on_screan()
        print(self.account_list.account[ANONYE_USERS].get_name())


    def run(self):
        print("open manage accounts")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        print("closing run")
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        print("closing manage accounts")


    def check_menu_action(self, action):
        event = self.get_button_from_position(ManageAccount.window_elements, action)
        if event == "main_menu":
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
        elif event != "no button":
            account_index = findall(r'\d+', event)[0]
            if search(".*name", event):
                self.edit_account(ANONYE_USERS + account_index)
            elif search(".*delete", event):
                self.delete_account(ANONYE_USERS + account_index)
            return False
        return True


    def get_account_list_on_screan(self): # kake, aber in einer liste hat es nicht funktionert
        for account_index in range(1, 6):
            try:
                eval(f"ManageAccount.account_{account_index}_name['text']['content'] = self.account_list.account[ANONYE_USERS + {account_index}].get_name()")
            except:
                eval(f"ManageAccount.account_{account_index}_name['text']['content'] = '+'")


    def set_account_list(self, account_list):
        self.account_list = account_list


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
