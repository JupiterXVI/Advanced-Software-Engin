"""
imports
"""
from adapter import GenericMenu
from gui import ChooseGame, MenuActions
from communication import Sender, Reseiver


class ChooseGameMenu(GenericMenu):
    """
    global variables
    """
    def __init__(self):
        self.chosen_game = "no game chosen"
        self.sender = Sender()
        self.reseiver = Reseiver()


    """
    functions
    """
    def change_menu(self):
        MenuActions.get_window_elements_on_screen(ChooseGame.window_elements, self.sender)


    def run(self):
        print("open choose game")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        print("closing choose game")
                    
    
    def check_menu_action(self, action):
        event = MenuActions.get_button_from_position(ChooseGame.window_elements, action)
        if event != "no button":
            if event == "start_menu":
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
            else:
                self.set_chosen_game(event) 
                self.sender.send(category='menu', name='game start', info={'function':'button_event', 'parameter':'game'})
            return True
        

    def set_chosen_game(self, game):
        self.chosen_game = game
    

    def get_chosen_game(self):
        return self.chosen_game
