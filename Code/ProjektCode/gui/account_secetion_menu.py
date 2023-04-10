"""
imports
"""
from core_files import Menu, AccountList
from adapter import GuiBuilder
from gui import AccountSelection
from communication import Sender, Reseiver

from re import findall


class AccountSelectionMenu(Menu):
    """
    global variables
    """
    def __init__(self, account_list:AccountList):
        self.selection = "not set"
        self.selectable_accounts = []
        self.users = account_list
        self.sender = Sender()
        self.reseiver = Reseiver()


    """
    functions
    """
    def change_menu(self):
        print("open selection screen")
        self.users.get_accounts()
        self.selectable_accounts = []
        self.get_selectable_accounts()
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':self.selectable_accounts})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})


    def run(self):
        print("start selection screen")
        self.selection = "not set"
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
                    print("close selection screen")
                    return
        self.sender.send(category="gui",name="clear window", info={'function':GuiBuilder.clear_window.__name__, 'parameter': ''})
        self.selectable_accounts = []
        print("close selection screen")
                    
    
    def check_menu_action(self, action):
        event = self.get_button_from_position(self.selectable_accounts, action)
        if event != "no button":
            account_index = int(findall(r'\d+', event)[0])+1
            self.selection = self.users.account[account_index]
            return True
        return False
    

    def get_selectable_accounts(self):
        account_index = -1
        for user in self.users.account:
            if account_index < 0:
                account_index += 1 
                continue
            account = AccountSelection.account_list[account_index]
            account['text']['content'] = user.get_name()
            self.selectable_accounts.append(account)
            account_index += 1 


    def get_selection(self):
        return self.selection
