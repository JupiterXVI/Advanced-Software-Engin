"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.account import Account


class Statistic():
    """
    global variables
    """
    def __init__(self, game_id, player_id):
        self.game_id = game_id
        self.player_id = player_id
        self.wins = 0
        self.losses = 0

    """
    functions
    """
    def get_wins(self):
        return self.wins

    def increase_wins(self):
        self.wins += 1

    def get_losses(self):
        return self.losses

    def increase_losses(self):
        self.losses += 1

    def reset_stats(self):
        self.wins = 0
        self.losses = 0


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    stat = Statistic(2, 2)
    print(stat.get_wins())
    stat.increase_wins()
    stat.increase_wins()
    print(stat.get_wins())
