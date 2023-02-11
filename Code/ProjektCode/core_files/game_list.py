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
        self.games.append(game)

    """
    # get accounts from database into a local list
    def get_games(self):
        games = self.datamanager.get_player_table()
        game_list = []
        for game in games:
            game_list.append(Game(game[0], game[1], player[2], player[3], player[4]))
        self.games = game_list

    # add account to local account list and to database
    def add_account(self, username, password, age, is_admin):
        self.datamanager.add_account(username, password, age, is_admin)
        player_id = self.datamanager.last_added_account()
        self.account.append(Account(player_id, username, password, age, is_admin))

    # save local data to database
    def save_account_data(self, account: Account):
        self.datamanager.update_account(account.player_id, account.name, account.password, account.age, account.is_admin)

    # remove account from local list and from database
    def delete_account(self, account_intex):
        to_be_deleted = self.account[account_intex]
        self.datamanager.delete_account(to_be_deleted.get_id())
        self.get_accounts()
        """