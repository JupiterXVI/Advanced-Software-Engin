"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.game import Game


class SpaceInvaders(Game):
    """
    global variables
    """
    def __init__(self, game_id, name, player_count):
        super().__init__(game_id, name, player_count)

    """
    functions
    """
    def play(self):
        print("aaaaah space invaders")

if __name__ == "__main__":
    space_inv = Game(1, "Space Invaders", 1)
    print(space_inv.__dict__)
    space_inv.start()