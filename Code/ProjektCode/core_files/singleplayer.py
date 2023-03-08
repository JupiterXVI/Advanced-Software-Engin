"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.playground import Playground


class Singleplayer(Playground):
    """
    global variables
    """
    def __init__(self, game):
        super().__init__(game)

    """
    functions
    """
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