"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from core_files.game import Game
from games.graphics import ChooseGraphicTTT



class TicTacToe(Game):
    """
    global variables
    """
    def __init__(self):
        super().__init__(
            game_id = 1, 
            name = "TicTacToe", 
            player_count = 2, 
            game_elements = ChooseGraphicTTT.game_elements
            )
        #
        self.field = [['','',''],['','',''],['','','']]

    """
    functions
    """
    def choose_field(self):
         pass

    def check_for_win(self):
        for column in range(2):
            if self.field[column][0] == self.field[column][1] and self.field[column][0] == self.field[column][2]:
                return True
            row = column
            if self.field[0][row] == self.field[1][row] and self.field[0][row] == self.field[2][row]:
                return True
        if self.field[1][1] == self.field[2][2] and self.field[1][1] == self.field[3][3]:
                return True
        if self.field[3][1] == self.field[2][2] and self.field[3][1] == self.field[1][3]:
                return True
        return False
    
    def player_act(self):
        self.choose_field()


        