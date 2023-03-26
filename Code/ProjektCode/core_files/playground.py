"""
imports
"""
#import wird zum Testen benötigt
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from adapter import GuiBuilder
from core_files import Singleplayer, Multiplayer
from communication import Sender, Reseiver


class Playground():
    """
    global variables
    """
    def __init__(self, game_list, gui:GuiBuilder):
        self.game_list = game_list
        self.sender = Sender()
        self.resiever = Reseiver()
        self.gui = gui

    """
    functions
    """
    def play(self, game_id):
        game = self.game_list[game_id]
        play_pattern = "no pattern set"
        if game.get_player_count() > 1:
            play_pattern = Multiplayer(game)
            self.connect_to_gui(play_pattern)
            #for user in range(game.player_count):
            #    player = self.choose_player()
            #    play_pattern.active_player(player)
        else:
            play_pattern = Singleplayer(game)
            self.connect_to_gui(play_pattern)
            #player = self.choose_player()
            #play_pattern.set_aktive_player(player)
        try:
            play_pattern.play()
        except:
            pass

    def connect_to_gui(self, play_pattern):
        play_pattern.sender.add_listener(self.gui.reseiver)
        self.gui.sender.add_listener(play_pattern.reseiver)

    def choose_player(self):
        pass
            