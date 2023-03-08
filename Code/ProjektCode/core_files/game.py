"""
imports
"""

class Game():
    """
    global variables
    """
    def __init__(self, game_id, name, player_count, game_elements):
        self.game_id = game_id
        self.name = name
        self.player_count = player_count
        self.game_elements = game_elements

    """
    functions
    """
    def get_name(self):
        return self.name

    def get_player_count(self):
        return self.player_count

    def start(self):
        print(self.name + " has been started")

    def pause(self):
        print(self.name + " has been paused")

    def player_act(self):
        pass

    def check_point(self):
        pass

    def check_win(self):
        pass