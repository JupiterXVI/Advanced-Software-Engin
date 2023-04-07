from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from adapter import Menu
from adapter import GuiBuilder
from gui import EditAccount
from communication import Sender, Reseiver
from re import search
from time import sleep

LETTER = 1
BACKSPACE = 9
COORDINATES = 2


class EditAccountMenu(Menu):

    def __init__(self):
        self.menu_interactables = "list of interactables"
        self.account = "not set"
        self.save_changes = False
        self.edit_mode = False
        self.edit_field = "not set"
        self.sender = Sender()
        self.reseiver = Reseiver()


    def change_menu(self):
        print("open edit account")
        self.get_current_account_values()
        self.update_screen_values()
        

    def update_screen_values(self):
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':EditAccount.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})


    def run(self):
        print("start edit account")
        self.edit_field = "not set"
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    print(f"message['info']: {message['info']}")
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        sleep(0.01) # wait for account data to be set bevor leaving
        print("stop edit account")


    def check_menu_action(self, action):
        if len(action) == COORDINATES:
            return self.click_action(action)
        elif len(action) in [LETTER, BACKSPACE]:
            self.type_action(action)
            self.update_screen_values()
            return False
            
            
    def click_action(self, action):
        event = self.get_button_from_position(EditAccount.window_elements, action)
        self.text_fiel_active(False, self.edit_field)
        if event == "no button":
            self.edit_mode = False
            self.edit_field = "not set"
            return False
        elif event == "cancel":
            return self.cancel()
        elif event == "save":
            return self.save()
        elif search("input_.*", event):
            self.edit_mode = True
            for field in EditAccount.input_fields:
                if event == field:
                    self.edit_field = EditAccount.input_fields[field]
                    self.text_fiel_active(True, self.edit_field)

    
    def save(self):
        self.save_changes = self.check_to_save()
        if self.save_changes:
            self.pass_canges_to_account()
            self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':'manage_account'})
            return True
        return False
    

    def cancel(self):
        self.get_current_account_values()
        self.save_changes = self.check_to_delete() 
        self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':'manage_account'})
        return True


    def type_action(self, action):
        if not self.edit_mode:
            return
        print(self.edit_field['text']['content'])
        if action == "backspace":
            self.edit_field['text']['content'] = self.edit_field['text']['content'][:-1]
        else:
            self.edit_field['text']['content'] = self.edit_field['text']['content']+action
        print(self.edit_field['text']['content'])
       

    def get_current_account_values(self):
        try:
            EditAccount.input_username['text']['content'] = str(self.account.get_name())
            EditAccount.input_password['text']['content'] =  str(self.account.get_password())
            EditAccount.input_password_repeat['text']['content'] =  str('')
            EditAccount.input_age['text']['content'] =  str(self.account.get_age())
            EditAccount.input_admin['text']['content'] =  str(self.account.get_admin())
        except:
            print("account is not set")


    def pass_canges_to_account(self):
        self.account.set_name(EditAccount.input_username['text']['content'])
        self.account.set_password(EditAccount.input_password['text']['content'])
        self.account.set_age(EditAccount.input_age['text']['content'])
        if EditAccount.input_admin['text']['content'] in ['True', 'true', 'T', 't', '1']:
            self.account.set_admin(True)
        else:
            self.account.set_admin(False)


    def text_fiel_active(self, active, text_field):
        if self.edit_field != "not set":
            if active:
                # make the text field lighter
                for color_index in range(3):
                    text_field["color"][color_index] += 30
            else:
                # make the text field darker
                for color_index in range(3):
                    text_field["color"][color_index] -= 30
                    self.edit_field = "not set"
            self.update_screen_values()
        


    def check_to_delete(self):
        if EditAccount.input_password['text']['content'] == str("") and EditAccount.input_username['text']['content'] == str(""):
            return False
        return True


    def check_to_save(self):
        if EditAccount.input_password["text"]["content"] == EditAccount.input_password_repeat["text"]["content"] and EditAccount.input_username["text"]["content"] != str(""):
            return True
        return False


    def has_been_changed(self):
        return self.save_changes


    def set_account(self, account):
        self.account = account


    def get_account(self):
        return self.account
    

    def get_to_save_account(self):
        return self.save_changes
    