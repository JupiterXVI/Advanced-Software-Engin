"""
imports
"""
#import wird zum Testen benötigt
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from adapter import GuiBuilder
from core_files import Singleplayer, Multiplayer


class Playground():
    """
    global variables
    """
    def __init__(self, game_list):
        self.game_list = game_list

    """
    functions
    """
    def choose_player(self):
        pass
    

    def play(self, game_id):
        game = self.game_list[game_id]
        play_pattern = "no pattern set"
        if game.player_count > 1:
            play_pattern = Multiplayer()
            #for user in range(game.player_count):
            #    player = self.choose_player()
            #    play_pattern.active_player(player)
        else:
            play_pattern = Singleplayer()
            #player = self.choose_player()
            #play_pattern.set_aktive_player(player)
        self.create_game_gamefield(game)
        play_pattern.play(game)

            
    def create_game_gamefield(self, game):
        #self.gui.set_game_elements(game.game_elements)
        #game_element_list = self.gui.create_game_elements()
        #self.gui.set_game_element_styles(game_element_list)
        #----
        #self.gui.update_window()
        #----
        pass


