"""
imports
"""
#from playground import Playground
from singleplayer import Singleplayer

class Account:
    """
    global variables
    """
    # bei erstellen eines Objekts der Klasse werden die Angaben durch den Spieler getroffen und in die Datenbank geschoben
    # können bei bedarf aus datenbank erfragt werden
    def __init__(self, player_id, name, password, age, is_admin):
        self.player_id = player_id
        self.name = name
        self.password = password
        self.age = age
        self.is_admin = is_admin

    """
    functions
    """
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
        return slef.age

    def set_admin(self, is_admin):
        self.is_admin = is_admin

    def save_user_data():
        pass 

    def save_user_stats():
        pass

print('--------------------------')
b = Singleplayer("a")
b.hallo()

