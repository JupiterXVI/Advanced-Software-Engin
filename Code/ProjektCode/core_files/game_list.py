"""
imports
"""
from adapter import DatabaseAccess
from core_files import Game


class GameList():
    """
    global variables
    """
    def __init__(self, datamanager: DatabaseAccess):
        self.datamanager = datamanager
        self.games = []


    """
    functions
    """
    def add_game(self, game: Game):
        self.add_to_list(game)
        #self.add_to_database(game)

    def add_to_list(self,  game: Game):
        self.games.append(game)

    def add_to_database(self, game):
        self.datamanager.get_game()
        #...