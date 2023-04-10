"""
imports
"""
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
    pass