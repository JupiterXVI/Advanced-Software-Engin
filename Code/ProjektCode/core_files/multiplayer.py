"""
imports
"""
from playground import Playground
from account import Account


class Multiplayer(Playground):
    """
    global variables
    """
    def __init__(self, game):
        self.active_player = []

    """
    functions
    """
    def add_player(self, new_player):
        self.active_player.append(new_player)

    def player_act(self):
        print("multiplayer action")


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    m = Multiplayer('Tic-Tac-Toe')      
    print(m.active_player)
    m.add_player(m.get_test_account())
    print(m.active_player)
    m.player_act()