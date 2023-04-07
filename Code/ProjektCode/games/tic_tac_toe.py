"""
imports
"""
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
            name = "tic_tac_toe", 
            player_count = 2, 
            )
        self.board = "no boerd initiliced"
        self.active_player = 'not set'
        self.win = "not set"
        self.funktion_with_parameters = [
            'player_act','calcualte_coordinates','position_active_symbol'
        ]
        

    """
    functions
    """
    def game_setup_values(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.active_player = 'X'
        self.win = {
            'winner':"no winner",
            'orientation':"not set",
            'line': 0
        }


    def game_setup_grafics(self):
        self.sender.send(category="gui",name="set window info", info={'function':GuiBuilder.set_window_info.__name__, 'parameter': ChooseGraphicTTT.tic_tac_toe_window})
        self.sender.send(category="gui",name="clear window", info={'function':GuiBuilder.clear_window.__name__, 'parameter': ''})
        self.sender.send(category="gui",name="draw board", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': ChooseGraphicTTT.tic_tac_toe_board})


    def run(self):
        active_game = True
        while active_game:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "game":
                    self.react_to_request(request=message['info'])
                elif message['category'] in ["exit","close_game"]:
                    active_game = False
                    print("closing game thread")


    def player_act(self, player_action):
        array_position = self.calcualte_coordinates(player_action)
        validity = False
        if self.position_active_symbol(array_position):
            self.draw_symbols()
            self.change_symbols()
            validity = True
        self.sender.send(category='action_validity', name='valid player action', info=validity)


    def calcualte_coordinates(self, general_position):
        x = int(general_position[0]/300)
        y = int(general_position[1]/300)
        array_position = (x,y)
        return array_position


    def position_active_symbol(self, position):
        if self.board[position[1]][position[0]] not in ['O','o','X','x']:
            self.board[position[1]][position[0]] = self.active_player
            return True
        else:
            return False


    def change_symbols(self):
        if self.active_player == 'O':
            self.active_player = 'X'
        else:
            self.active_player = 'O'


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
                    self.sender.send(category="gui", name="draw symbol", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': symbol})


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
            self.sender.send(category="win", name="winning info", info={'win':False, 'waiting_on_win':False, 'player_points':[0,0]})
            for row in range(DIMENSION):
                for col in range(DIMENSION):
                    if self.board[row][col] != 'x' and self.board[row][col] != 'o':
                        return "no winner"
        else:
            points = [0,0]
            if self.win['winner'] in ['X','x']:
                points = [1,0]
            else:
                points = [0,1]
            self.sender.send(category="win", name="winning info", info={'win':True, 'waiting_on_win':False, 'player_points':points})


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
                self.sender.send(category="gui", name="ttt win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'vertical'): 
            for row in range(DIMENSION):
                winner_image['position'] = ChooseGraphicTTT.positions[row][self.win['line']]
                self.sender.send(category="gui", name="ttt win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'diagonal_tl-br'): 
            for i in range(DIMENSION): 
                winner_image['position'] = ChooseGraphicTTT.positions[i][i]
                self.sender.send(category="gui", name="ttt win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
        elif(self.win['orientation'] == 'diagonal_bl-tr'): 
            for i in range(DIMENSION): 
                winner_image['position'] = ChooseGraphicTTT.positions[2-i][i]
                self.sender.send(category="gui", name="ttt win", info={'function':GuiBuilder.load_image_on_screen.__name__, 'parameter': winner_image})
