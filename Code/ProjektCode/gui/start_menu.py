"""
imports
"""
from core_files import Menu
from adapter import GuiBuilder
from gui import Start
from communication import Sender, Reseiver


# this class is the zentral menu from which the user can access the games and other options,
# as well as the zentrall data forwareder between games and the playground
class StartMenu(Menu):
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
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':Start.window_elements})
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
        event = self.get_button_from_position(Start.window_elements, action)
        if event != "no button":
            if event == "exit":
                self.sender.send(category="exit", name="exit_event", info="window_closed")
            else:
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
            return True
        

if __name__ == "__main__":
    pass