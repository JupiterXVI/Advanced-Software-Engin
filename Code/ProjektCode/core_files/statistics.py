"""
imports
"""
from adapter import DatabaseAccess
from core_files import GameStatistic


class Statistics():
    """
    global variables
    """
    def __init__(self, datamanager: DatabaseAccess):
        self.datamanager = datamanager
        self.player_game_stats = []


    """
    functions
    """
    # get accounts from database into a local list
    def get_statistics(self):
        stats = self.datamanager.get_game_stat_table()
        stat_list = []
        for stat in stats:
            stat_list.append(GameStatistic(stat[0], stat[1], stat[2], stat[3]))
        self.player_game_stats = stat_list

    def get_wins(self):
        return self.wins


    def increase_wins(self, player_id, game_id):
        for entry in self.player_game_stats:
            if entry.get_player_id() == player_id and entry.get_game_id() == game_id:
                entry.increase_wins()
        self.datamanager.add_win(player_id, game_id)


    def increase_losses(self, player_id, game_id):
        for entry in self.player_game_stats:
            if entry.get_player_id() == player_id and entry.get_game_id() == game_id:
                entry.increase_losses()
        self.datamanager.add_loss(player_id, game_id)


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    pass
