"""
imports
"""
from gui import WinScreenMenu, WinScreen, MenuActions

from random import random
from time import sleep


class WinScreenMenuDisco(WinScreenMenu):
    """
    global variables
    """
    def __init__(self):
        super(WinScreenMenuDisco, self).__init__()
        self.player_score_elements = []

    """
    functions
    """
    def run(self):
        print("start win screen")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
            self.change_title_color()
            sleep(0.2)
        self.player_score_elements = []
        print("close win screen")


    def change_title_color(self):
        WinScreen.congretulation['text']['color'] = self.random_rgb_color()
        MenuActions.get_window_elements_on_screen(WinScreen.window_elements + self.player_score_elements, self.sender)


    def random_rgb_color(self):
        color = []
        for rgb_value in range(3):
            color_value = int(random()*255)
            color.append(color_value)
        return color
