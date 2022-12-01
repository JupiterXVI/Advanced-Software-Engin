from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import Menu
from adapter import AllowToBuldMenu
from gui import ChooseGameMenu

class ChooseGame(Menu):
    def __init__(self, gui: AllowToBuldMenu):
        self.gui = gui

    def open_menu(self):
        print(ChooseGameMenu.hallo)
        

    def run_menu(self):
        pass

    def close_menu(self):
        pass