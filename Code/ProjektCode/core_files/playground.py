"""
imports
"""
#import wird zum Testen benötigt
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from core_files.account import Account


class Playground():
    """
    global variables
    """
    def __init__(self, game):
        self.game = game
        self.active_player = None

    """
    functions
    """
    def open_menu(self, game):
        pass

    def create_game_gamefield(self):
        pass

    def player_act(self):
        print("player does action")

#funktion zum Testen benötigt    
    def get_test_account(self):
        a = Account(2, "Jimmy", "jimTheGreat", "15", True)
        return a