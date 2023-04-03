"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from time import sleep 
from adapter import Menu
from adapter import GuiBuilder
from gui import MainMenu

from communication import Sender, Reseiver

# this class is the zentral menu from which the user can access the games and other options,
# as well as the zentrall data forwareder between games and the playground
class GameLibraryMenu(Menu):
    """
    global variables
    """
    def __init__(self):
        self.sender = Sender()
        self.reseiver = Reseiver()
        

    """
    functions
    """
    # hier könnte man auch noch open/closed-Principle verwenden
    # -> eine Liste mit bilding-functions um das Menu stück für Stück zu bauen
    # this funktion uses the gui objekt to create a menu form the class parameters
    def change_menu(self):
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':MainMenu.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})


    def run(self):
        print("open game library")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        print("closing game library")


    def check_menu_action(self, action):
        event = self.get_button_from_position(MainMenu.window_elements, action)
        if event != "no button":
            if event == "exit":
                self.sender.send(category="exit", name="exit_event", info="window_closed")
            else:
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
            return True
        






    # this funktion is the loop to run the main menu, checking for user interaktion
    def run_menu(self):
        print("running main menu...")
        main_menu_active = True
        action = "waiting for action"
        while main_menu_active:
            self.gui.update_window()
            action = self.gui.check_events(self.menu_interactables)
            if action != "no action":
                if action == "quit":               
                    self.gui.terminate_window()
                if action == "choose_game_button":
                    self.gui.clear_window()
                    self.menu_interactables = []
                    self.choose_game.open_menu()
                    self.choose_game.run_menu()
                    self.open_menu()
                    sleep(Menu.blocking_wait_seconds)
                if action == "account_button":
                    print("account")
                    self.gui.clear_window()
                    self.menu_interactables = []
                    self.manage_account.open_menu()
                    self.manage_account.run_menu()
                    self.open_menu()
                    sleep(Menu.blocking_wait_seconds)
                if action == "exit_button":
                    print("exit")
                    main_menu_active = False
                if action == "circle_button":
                    print("circle")
            sleep(Menu.allow_passes_per_second)
        self.close_menu()



if __name__ == "__main__":
    pass