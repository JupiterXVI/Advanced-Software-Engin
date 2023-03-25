"""
imports
"""
from adapter import DatabaseAccess
from core_files import Game


class GameList():
    """
    global variables
    """
    # bei erstellen eines Objekts der Klasse werden die Angaben durch den Spieler getroffen und in die Datenbank geschoben
    # können bei bedarf aus datenbank erfragt werden
    def __init__(self, datamanager: DatabaseAccess):
        self.datamanager = datamanager
        self.games = []


    """
    functions
    """
    def add_game(self, game: Game):
        self.add_to_list(game)
        self.add_to_database(game)

    def add_to_list(self,  game: Game):
        self.games.append(game)

    def add_to_database(self):
        self.datamanager.get_game()
        #...