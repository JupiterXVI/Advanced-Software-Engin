"""
imports
"""
from adapter import Manager, GenericMenu, ManageMenu, EditMenu, GuiBuilder
from communication import Sender, Reseiver
from gui import Window


class MenuManager(Manager):
    """
    global variables
    """
    def __init__(self, gui:GuiBuilder, start_menu:GenericMenu, choose_game:GenericMenu, manage_account:ManageMenu, edit_account:EditMenu):
        self.gui =  gui
        
        self.start_menu = start_menu
        self.choose_game = choose_game
        self.manage_account = manage_account
        self.edit_account = edit_account
        
        self.next_menu = self.start_menu
        self.sender = Sender()
        self.reseiver = Reseiver()
        # if set to false, gui will close because main loop ends  
        self.come_back_to_menu = True


    """
    functions
    """
    def setup_window(self):
        self.sender.send(category='gui',name='send window_info', info={'function':GuiBuilder.set_window_info.__name__, 'parameter':Window.info})
        self.sender.send(category='gui', name='create window', info={'function':GuiBuilder.create_window.__name__, 'parameter':''})


    def clear_window(self):
        self.sender.send(category='gui',name='send window_info', info={'function':GuiBuilder.set_window_info.__name__, 'parameter':Window.info})
        self.sender.send(category="gui",name="clear window", info={'function':GuiBuilder.clear_window.__name__, 'parameter': ''})


    def open_menus(self):
        print("open manager")
        self.clear_window()
        active_menu = self.next_menu
        while self.next_menu != "no menu":
            try:
                self.sender.add_listener(active_menu.reseiver)
                active_menu.sender.add_listener(self.reseiver)
                active_menu.change_menu()
                active_menu.reseiver.empty_message_queue()

                if not self.should_come_back_to_menu():
                    print("closing manager")
                    return
                    
                active_menu.run()
            except:
                "no menu is set on menu start"
            try:
                self.sender.remove_listener(active_menu.reseiver)
                active_menu.sender.remove_listener(self.reseiver)
            except:
                "no menu is set on menu close"
            active_menu = self.next_menu

        self.set_next_menu("start_menu")
        print("closing manager")


    def set_next_menu(self, menu):
        if menu == "start_menu":
            self.next_menu = self.start_menu
        if menu == "choose_game":
            self.next_menu = self.choose_game
        elif menu == "manage_account":
            self.manage_account.set_to_save_account(self.edit_account.get_to_save_account())
            self.next_menu = self.manage_account
        elif menu == "edit_account":
            self.next_menu = self.edit_account
            self.edit_account.set_account(self.manage_account.get_selected_account())
        elif menu == "game":
            self.next_menu = "no menu"
        elif menu == "exit":
            self.next_menu = "no menu"
            self.come_back_to_menu = False


    def run_relay(self):
        self.sender.add_listener(self.gui.reseiver)
        self.gui.sender.add_listener(self.reseiver)
        active_relay = True
        while active_relay:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "menu":
                    self.set_next_menu(message['info']['parameter'])
                elif message['category'] == "gui":
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                elif message['category'] == "input":
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                elif message['category'] == "exit":
                    active_relay = False
                    self.set_next_menu("exit")
                    self.sender.send(category="exit", name="exit_event", info="window_closed")
                    print("closing manager relay thread")


    def should_come_back_to_menu(self):
        return self.come_back_to_menu
    


if __name__ == "__main__":
    print("the menu manager coordinates the changing of menu screens.")