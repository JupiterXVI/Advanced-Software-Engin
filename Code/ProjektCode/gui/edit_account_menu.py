from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from re import search
from time import sleep

from adapter import Menu
from adapter import GuiBuilder
from gui import EditAccount
from core_files import Account

from communication import Sender, Reseiver

class EditAccountMenu(Menu):   # mit vererbung könnten die __init__, open- close_menu funktionen ausgelassen werden
    def __init__(self):
        #self.gui = gui #gebraucht?
        self.menu_interactables = "list of interactables"
        self.account = "Not Set"
        self.save_changes = False

        self.sender = Sender()
        self.reseiver = Reseiver()


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
            # make the text field lighter
            for color_index in range(3):
                text_field["color"][color_index] += 30
        else:
            # make the text field darker
            for color_index in range(3):
                text_field["color"][color_index] -= 30

    def enter_text(self, text_field):
        self.text_fiel_active(True, text_field)
        sleep(Menu.blocking_wait_seconds)
        still_tiyping = True
        while still_tiyping:
            action = self.gui.check_events(self.menu_interactables)
            self.gui.set_element_styles()
            self.gui.update_window()
            sleep(Menu.allow_passes_per_second)
            if action == "quit":               # kommt man von diesem if wald weg?
                self.gui.terminate_window()
            if search("^.$", action):
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


    def change_menu(self):
        #self.gui.set_window_elements(EditAccount.window_elements)
        #self.menu_interactables = self.gui.create_window_interaction_elements()
        self.get_account_values_on_screen()
        #self.gui.set_element_styles()
        #self.gui.update_window()
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':EditAccount.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})

        

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
                    menu_in_use = False
                    print("closing menu thread")







    def run_menu(self):
        sleep(Menu.blocking_wait_seconds)
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
            sleep(Menu.allow_passes_per_second)
        self.close_menu()

    def has_been_changed(self):
        return self.save_changes

    def close_menu(self):
        self.gui.clear_window()
        self.menu_interactables = []