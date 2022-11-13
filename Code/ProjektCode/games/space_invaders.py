"""
imports
"""
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
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