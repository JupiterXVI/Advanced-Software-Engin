"""
imports
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    """
    global variables
    """


    """
    functions
    """
    @abstractmethod
    def change_menu(self):
        pass


    @abstractmethod
    def run(self):
        pass


    def get_button_from_position(self, button_list, position):
        x, y = position
        for button in button_list:
            if (x > button['position'][0] and 
                x < (button['position'][0] + button['dimensions'][0]) and
                y > button['position'][1] and 
                y < (button['position'][1] + button['dimensions'][1])):
                return button['name']
        return "no button"
