"""
imports
"""
from communication import Sender, Reseiver

class Game():
    """
    global variables
    """
    def __init__(self, game_id, name, player_count):
        self.game_id = game_id
        self.name = name
        self.player_count = player_count
        self.sender = Sender()
        self.reseiver = Reseiver()
        self.funktion_with_parameters = []

    """
    functions
    """
    def get_name(self):
        return self.name

    def get_player_count(self):
        return self.player_count

    def game_setup_values(self):
        print("setting all starter values")

    def game_setup_grafics():
        print("prepare game graphicaly")

    def run(self):
        print(self.name + " has been started")

    def react_to_request(self, request):
        if request["function"] in self.funktion_with_parameters:
            eval(f"self.{request['function']}")(request['parameter'])
        else:
            eval(f"self.{request['function']}")()

    def player_act(self):
        pass

    def check_win(self):
        pass
