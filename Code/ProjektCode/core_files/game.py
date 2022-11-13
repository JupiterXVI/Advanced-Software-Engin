"""
imports
"""

class Game():
    """
    global variables
    """
    def __init__(self, game_id, name, player_count):
        self.game_id = game_id
        self.name = name
        self.player_count = player_count

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