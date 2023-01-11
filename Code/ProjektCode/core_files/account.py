"""
imports
"""
from adapter import DatabaseAccess


class Account():
    """
    global variables
    """
    # bei erstellen eines Objekts der Klasse werden die Angaben durch den Spieler getroffen und in die Datenbank geschoben
    # können bei bedarf aus datenbank erfragt werden
    def __init__(self, player_id, name, password, age, is_admin): #datamanager: DatabaseAccess
        self.player_id = player_id
        self.name = name
        self.password = password
        self.age = age
        self.is_admin = is_admin
        #self.datamanager = datamanager
        #self.add_account()


    """
    functions
    """
    #def add_account(self):
    #    self.datamanager.add_account(self.player_id, self.name, self.password, self.age, self.is_admin)

    #def save_account_data(self):
    #    self.datamanager.update_account(self.player_id, self.name, self.password, self.age, self.is_admin)

    def refresh_account_data(self):
        pass

    def get_id(self):
        return self.player_id

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_password(self, new_password):
        self.password = new_password

    def get_password(self):
        return self.password

    def set_age(self, new_age):
        self.age = new_age

    def get_age(self):
        return self.age

# koherenz erhöhen durch auslagerung des Adminkontents in eigenes Element 
    def set_admin(self, is_admin):
        self.is_admin = is_admin

    def get_admin(self):
        return self.is_admin

# die funktionen sollen vermutlich nicht hier her
    def save_user_stats(self):
        pass
    