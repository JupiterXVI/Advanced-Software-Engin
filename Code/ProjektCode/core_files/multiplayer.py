"""
imports
"""
from .playground import Playground



class Multiplayer(Playground):
    """
    global variables
    """
    def __init__(self, game):
        self.game = game
        self.active_player = []
        self.player_points = []
        self.playing = True

    """
    functions
    """
    #TODO spiele auswählen
    def select_player(self):
        for player in range(self.game.player_count):
            # select screen
            # add_player(from select screen)
            pass

    def add_player(self, new_player):
        self.active_player.append(new_player)
        self.player_points.append(0)

    def show_result(self):
        # show result screen
        pass

    def play(self):
        self.select_player()
        while self.playing:
            for player in range(len(self.active_player)-1):
                self.game.player_act()
                self.player_points[player] += self.game.check_point()
                if self.game.check_win():
                    self.playing = False
                    break
        self.show_result()


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    m = Multiplayer('Tic-Tac-Toe')      
    print(m.active_player)
    m.add_player(m.get_test_account())
    print(m.active_player)
    m.player_act()