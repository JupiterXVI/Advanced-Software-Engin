"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from adapter import Menu
from adapter import GuiBuilder
from communication import Sender, Reseiver

class MenuManager():
    """
    global variables
    """
    def __init__(self, gui:GuiBuilder, main_menu:Menu, choose_game:Menu, manage_account:Menu, edit_account:Menu):
        # objekt of a class which can visualize the menus/games
        self.gui =  gui
        self.main_menu = main_menu
        self.choose_game = choose_game
        self.manage_account = manage_account
        self.edit_account = edit_account

        self.active_menu = self.main_menu

        self.sender = Sender()
        self.reseiver = Reseiver()


    """
    functions
    """
    def setup_window(self, window):
        self.sender.send(category='gui',name='send window_info', info={'function':GuiBuilder.set_window_info.__name__, 'parameter':window.info})
        self.sender.send(category='gui', name='create window', info={'function':GuiBuilder.create_window.__name__, 'parameter':''})


    def open_menus(self):
        print("open manager")
        while self.active_menu != "no menu":
            try:
                self.sender.add_listener(self.active_menu.reseiver)
                self.active_menu.sender.add_listener(self.reseiver)
                self.active_menu.change_menu()
                self.active_menu.reseiver.empty_message_queue()
                self.active_menu.run()
            except:
                "no menu is set on menu start"
            try:
                self.sender.remove_listener(self.active_menu.reseiver)
                self.active_menu.sender.remove_listener(self.reseiver)
            except:
                "no menu is set on menu close"
        print("closing manager")


    def set_active_menu(self, menu):
        if menu == "main_menu":
            self.active_menu = self.main_menu
        if menu == "choose_game":
            self.active_menu = self.choose_game
        elif menu == "account":
            self.active_menu = self.manage_account
        elif menu == "edit_account":
            self.active_menu = self.edit_account
        elif menu == "exit":
            self.active_menu = "no menu"


    def run_relay(self):
        self.sender.add_listener(self.gui.reseiver)
        self.gui.sender.add_listener(self.reseiver)
        active_relay = True
        while active_relay:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "menu":
                    self.set_active_menu(message['info']['parameter'])
                elif message['category'] == "gui":
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                elif message['category'] == "input":
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                elif message['category'] == "exit":
                    self.set_active_menu("exit")
                    self.sender.send(category="exit", name="exit_event", info="window_closed")
                    active_relay = False
                    print("closing manager relay thread")
