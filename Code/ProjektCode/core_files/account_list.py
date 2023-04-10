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
    # get accounts from database into a local list
    def get_accounts(self):
        players = self.datamanager.get_player_table()
        player_list = []
        for player in players:
            player_list.append(Account(player[0], player[1], player[2], player[3], player[4]))
        self.account = player_list

    # add account to local account list and to database
    def add_account(self, username, password, age, is_admin):
        if len(self.account) <= 8:
            self.datamanager.add_account(username, password, age, is_admin)
            player_id = self.datamanager.last_added_account()
            self.datamanager.add_account_gamestats(player_id)
            self.account.append(Account(player_id, username, password, age, is_admin))
        else:
            print("maximum of usable accounts has been reached")

    # save local data to database
    def save_account_data(self, account: Account):
        self.datamanager.update_account(account.player_id, account.name, account.password, account.age, account.is_admin)

    # remove account from local list and from database
    def delete_account(self, account):
        self.datamanager.delete_account(account.get_id())
        self.get_accounts()
    