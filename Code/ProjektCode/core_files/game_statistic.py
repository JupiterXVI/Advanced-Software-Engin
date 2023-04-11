"""
imports
"""


class GameStatistic():
    """
    global variables
    """
    def __init__(self, player_id, game_id, wins, losses):
        self.player_id = player_id
        self.game_id = game_id
        self.wins = wins
        self.losses = losses


    """
    functions
    """
    def get_player_id(self):
        return self.player_id
    

    def get_game_id(self):
        return self.game_id
    

    def get_wins(self):
        return self.wins


    def increase_wins(self):
        self.wins += 1


    def get_losses(self):
        return self.losses


    def increase_losses(self):
        self.losses += 1



# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    pass
