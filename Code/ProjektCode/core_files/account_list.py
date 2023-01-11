"""
imports
"""
from adapter import DatabaseAccess
from core_files import Account


class AccountList():
    """
    global variables
    """
    # bei erstellen eines Objekts der Klasse werden die Angaben durch den Spieler getroffen und in die Datenbank geschoben
    # können bei bedarf aus datenbank erfragt werden
    def __init__(self, datamanager: DatabaseAccess):
        self.datamanager = datamanager
        self.account = []

    """
    functions
    """
    def get_accounts(self):
        players = self.datamanager.get_player_table()
        player_list = []
        for player in players:
            player_list.append(Account(player[0], player[1], player[2], player[3], player[4]))
        self.account = player_list

    def add_account(self, player_id, username, password, age, is_admin):
        self.datamanager.add_account(player_id, username, password, age, is_admin)
        self.account.append(Account(player_id, username, password, age, is_admin))

    def save_account_data(self, account: Account):
        self.datamanager.update_account(account.player_id, account.name, account.password, account.age, account.is_admin)

    def refresh_account_data(self):
        pass

    