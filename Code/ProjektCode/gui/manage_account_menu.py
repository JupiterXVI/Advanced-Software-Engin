"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import Menu
from adapter import AllowToBuldMenu
from gui import ManageAccount

class ManageAccountMenu(Menu):
    """
    global variables
    """
    def __init__(self, gui: AllowToBuldMenu):
        self.gui = gui
        
    """
    functions
    """
    def open_menu(self):
        print(ManageAccount.window_elements)
        pass

    def run_menu(self):
        pass

    def close_menu(self):
        pass