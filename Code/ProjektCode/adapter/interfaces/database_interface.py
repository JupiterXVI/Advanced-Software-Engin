"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class DatabaseAccess(ABC):
    @abstractmethod
    def add_account(self, username, password, age, is_admin):
        pass
    
    @abstractmethod
    def add_account_gamestats(self, player_id):
        pass

    @abstractmethod
    def last_added_account(self):
        pass

    @abstractmethod
    def update_account(self, player_id, username, password, age, is_admin):
        pass
    
    @abstractmethod
    def delete_account(self, player_id):
        pass

    @abstractmethod
    def get_player_table(self):
        pass

    @abstractmethod
    def get_player(self, player_id):
        pass

    @abstractmethod
    def get_game_table(self):
        pass

    @abstractmethod
    def get_game(self, game_name):
        pass

    @abstractmethod
    def get_game_stat_table(self):
        pass

    @abstractmethod
    def get_game_stat(self, player_id, game_id):
        pass

    @abstractmethod
    def add_win(self, player_id, game_id):
        pass

    @abstractmethod
    def add_loss(self, player_id, game_id):
        pass
