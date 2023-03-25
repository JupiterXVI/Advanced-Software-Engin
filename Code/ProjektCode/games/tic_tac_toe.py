"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import GuiBuilder
from core_files.game import Game
from games.graphics import ChooseGraphicTTT

DIMENSION = 3

class TicTacToe(Game):
    """
    global variables
    """
    def __init__(self):
        super().__init__(
            game_id = 1, 
            name = "TicTacToe", 
            player_count = 2, 
            )
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.active_player = 'X'
        self.win = {
            'winner':"no winner",
            'orientation':"not set",
            'line': 0
        }
        self.funktion_with_parameters = [
            'calcualte_coordinates','position_active_symbol'
        ]
        

    """
    functions
    """
    def run(self):
        while True:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "game":
                    self.react_to_request(request=message['info'])

    def react_to_request(self, request):
        if request["function"] in self.funktion_with_parameters:
            eval(f"self.{request['function']}")(request['parameter'])
        else:
            eval(f"self.{request['function']}")()


    def choose_field(self):
         pass
    

    def calcualte_coordinates(self, general_position):
        x = int(general_position[0]/300)
        y = int(general_position[1]/300)
        array_position = (x,y)
        print(array_position)
        return array_position
    

    def position_active_symbol(self, general_position):
        array_position = self.calcualte_coordinates(general_position)

        if self.board[array_position[1]][array_position[0]] not in ['O','o','X','x']:
            self.board[array_position[1]][array_position[0]] = self.active_player
            return True
        else:
            return False
        

    def change_symbols(self):
        if self.active_player == 'O':
            self.active_player = 'X'
        else:
            self.active_player = 'O'


    def draw_board(self):
        self.sender.send(category="gui",name="draw_board", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': ChooseGraphicTTT.tic_tac_toe_board})


    def draw_symbols(self):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                if self.board[row][col] not in [0, "x", "o"]:
                    symbol = "no symbol"
                    if self.board[row][col] == 'O':
                        self.board[row][col] = 'o'
                        symbol = ChooseGraphicTTT.tic_tac_toe_o
                    elif self.board[row][col] == 'X':
                        self.board[row][col] = 'x'
                        symbol = ChooseGraphicTTT.tic_tac_toe_x
                    symbol['position'] = ChooseGraphicTTT.positions[row][col]
                    self.sender.send(category="gui", name="draw_symbol", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': symbol})


    def check_win(self):
        for row in range(DIMENSION):
            if((self.board[row][0] == self.board[row][1] == self.board[row][2]) and (self.board[row][0] != 0)):
                self.win['winner'] = self.board[row][0]
                self.win['orientation'] = "horizontal"
                self.win['line'] = row

        for col in range(DIMENSION):
            if((self.board[0][col] == self.board[1][col] == self.board[2][col]) and (self.board[0][col] != 0)):
                self.win['winner'] =  self.board[0][col]
                self.win['orientation'] = "vertical"
                self.win['line'] = col
   
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] != 0):
            self.win['winner'] =  self.board[0][0]
            self.win['orientation'] = "diagonal_tl-br"
          
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] != 0):
            self.win['winner'] =  self.board[0][2]
            self.win['orientation'] = "diagonal_bl-tr"
    
        if self.win['winner'] == "no winner":
            for row in range(DIMENSION):
                for col in range(DIMENSION):
                    if self.board[row][col] != 'x' and self.board[row][col] != 'o':
                        return "no winner"
            return "DRAW"
        
        print(f"The winner is: {self.win['winner']} !!!")

        # self.update_window
    

    def player_act(self):
        self.choose_field()


    def update_window(self):
        self.sender.send(category="gui", name="update_window", info={'function':GuiBuilder.update_window.__name__, 'parameter':''})


    def draw_win(self):
        if self.win['winner'] == "no winner":
            return
        winner_image = "not yet chosen"
        if self.win['winner'] in ['X','x']:
            winner_image = ChooseGraphicTTT.tic_tac_toe_x_winning
        else:
            winner_image = ChooseGraphicTTT.tic_tac_toe_o_winning

        if (self.win['orientation'] == 'horizontal'):
            for col in range(DIMENSION):
                winner_image['position'] = ChooseGraphicTTT.positions[self.win['line']][col]
                self.sender.send(category="gui", name="ttt_win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'vertical'): 
            for row in range(DIMENSION):
                winner_image['position'] = ChooseGraphicTTT.positions[row][self.win['line']]
                self.sender.send(category="gui", name="ttt_win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'diagonal_tl-br'): 
            for i in range(DIMENSION): 
                winner_image['position'] = ChooseGraphicTTT.positions[i][i]
                self.sender.send(category="gui", name="ttt_win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'diagonal_bl-tr'): 
            for i in range(DIMENSION): 
                winner_image['position'] = ChooseGraphicTTT.positions[2-i][i]
                self.sender.send(category="gui", name="ttt_win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
