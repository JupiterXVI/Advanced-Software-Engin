"""
imports
"""
from adapter import ManageMenu
from gui import ManageAccount, MenuActions
from communication import Sender, Reseiver
from re import search, findall

FIRST_AVAILABLE_USERS = 3
POSSIBLE_USERS = 5


class ManageAccountMenu(ManageMenu):
    """
    global variables
    """
    def __init__(self):
        self.account_list = "not set"
        self.save_account = False
        self.selected_account = "no account selected"
        self.sender = Sender()
        self.reseiver = Reseiver()

        
    """
    functions
    """
    def change_menu(self):
        print("open manage accounts")
        self.handle_previous_edit()
        self.update_menu_screen()
             

    def run(self):
        print("start manage accounts")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        print("stop manage accounts")


    def check_menu_action(self, action):
        event = MenuActions.get_button_from_position(ManageAccount.window_elements, action)
        if event == "start_menu":
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
                return True
        elif event != "no button":
            account_index = int(findall(r'\d+', event)[0])
            if search(".*name", event):
                self.edit_account(FIRST_AVAILABLE_USERS + account_index)
                return True
            elif search(".*delete", event):
                self.delete_account(FIRST_AVAILABLE_USERS + account_index)
        return False
        

    def get_account_list_on_screen(self):
        for account_index in range(POSSIBLE_USERS):
            try:
                ManageAccount.account_button_list[account_index]['text']['content'] = self.account_list.account[FIRST_AVAILABLE_USERS + account_index].get_name()
            except:
                ManageAccount.account_button_list[account_index]['text']['content'] = '+'


    def set_account_list(self, account_list):
        self.account_list = account_list


    def edit_account(self, account_index):
        if account_index < len(self.account_list.account):
            self.selected_account = self.account_list.account[account_index]
        else:
            self.account_list.add_account("", "", "", False)
            self.selected_account = self.account_list.account[len(self.account_list.account)-1]
        self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':"edit_account"})


    def handle_previous_edit(self):
        if type(self.selected_account) == type(""):
            return
        if self.save_account:
            self.account_list.save_account_data(self.selected_account)
        else:
            self.account_list.delete_account(self.selected_account)
        self.save_account = False
        self.selected_account = "not selected"


    def delete_account(self, account_index):
        if account_index < len(self.account_list.account):
            account = self.account_list.account[account_index]
            self.account_list.delete_account(account)
        self.update_menu_screen()


    def update_menu_screen(self):
        self.get_account_list_on_screen()
        MenuActions.get_window_elements_on_screen(ManageAccount.window_elements, self.sender)


    def set_selected_account(self, account):
        self.selected_account = account


    def get_selected_account(self):
        return self.selected_account


    def set_to_save_account(self, should_save):
        self.save_account = should_save
