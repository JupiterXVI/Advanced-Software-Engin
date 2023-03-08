"""
imports
"""
#import wird zum Testen benötigt
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from adapter import AllowToBuldMenu


class Playground():
    """
    global variables
    """
    def __init__(self, game_list, gui = AllowToBuldMenu,):
        self.gui = gui
        self.game_list = game_list
        self.active_player = None

    """
    functions
    """
    def choose_player(self):
        pass

    def play(self, game_id):
        game = self.game_list[game_id]
        self.open_menu(game)
        game.start()
        self.player_act()

    def open_menu(self, game):
        self.gui.set_game_elements(game.game_elements)
        game_element_list = self.gui.create_game_elements()
        self.gui.set_game_element_styles(game_element_list)
        #----
        self.gui.update_window()
        #----

    def create_game_gamefield(self):
        pass

    def player_act(self):
        while True:
            self.gui.update_window()
        print("player does action")
