"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class DatabaseAccess(ABC):
    @abstractmethod
    def add_account(self, player_id, username, password, age, is_admin):
        pass

    def update_account(self, player_id, username, password, age, is_admin):
        pass
    
    def get_player_table(self):
        pass

    def get_player(self, player_id):
        pass

    def get_game_table(self):
        pass

    def get_game(self, game_id):
        pass

    def get_game_stat_table(self):
        pass

    def  get_game_stat(self, player_id, game_id):
        pass