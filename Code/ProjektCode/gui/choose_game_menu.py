from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from time import sleep

from adapter import Menu
from adapter import GuiBuilder
from gui import ChooseGame

from communication import Sender, Reseiver

class ChooseGameMenu(Menu):
    def __init__(self):
        self.chousen_game = "no game chousen"
        self.sender = Sender()
        self.reseiver = Reseiver()


    def change_menu(self):
        self.sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':ChooseGame.window_elements})
        self.sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})


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
        event = self.get_button_from_position(ChooseGame.window_elements, action)
        if event != "no button":
            if event == "main_menu":
                self.sender.send(category='menu', name='change menu', info={'function':'button_event', 'parameter':event})
            else:
                self.set_chousen_game(event) 
                self.sender.send(category='menu', name='game start', info={'function':'button_event', 'parameter':'game'})
            return True
        

    def set_chousen_game(self, game):
        self.chousen_game = game
    

    def get_chousen_game(self):
        return self.chousen_game
