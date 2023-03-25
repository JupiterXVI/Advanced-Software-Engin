"""
imports
"""

class Singleplayer():
    """
    global variables
    """
    def __init__(self, game):
        self.game = game
        self.active_player = "no player set"

    """
    functions
    """
    def play(self):
        pass

    def set_aktive_player(self, aktive_player):
        self.active_player = aktive_player

    def player_act(self):
        print("singleplayer action")


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    s = Singleplayer('SpaceInvaders')
    a = s.get_test_account()
    print(s.active_player)
    s.set_aktive_player(a)
    print(s.active_player)
    s.player_act()  