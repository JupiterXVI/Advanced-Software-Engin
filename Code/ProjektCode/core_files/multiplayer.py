"""
imports
"""
from core_files import Game
from communication import Sender, Reseiver
from threading import Thread
from time import sleep


#from core_files import AccountList
#from adapter import PostgreSqlAdapter


class Multiplayer():
    """
    global variables
    """
    def __init__(self):
        self.game = "not set"
        self.active_player = []
        self.player_points = []
        self.win_info = "not set"
        self.game_is_running = True
        self.valid_player_action = False
        self.player_is_acting = False
        self.player_action = "no player action"
        self.sender = Sender()
        self.reseiver = Reseiver()
        self.active_relay = "not started"
        self.interrupt_exit = False


    """
    functions
    """
    def set_game(self, game):
        self.game = game

    
    def get_game(self):
        return self.game


    def get_active_player(self):
        return self.active_player
    

    def get_points(self):
        return self.player_points
    

    def add_player(self, new_player):
        self.active_player.append(new_player)
        self.player_points.append(0)
        

    def reset_game(self):
        self.active_player = []
        self.player_points = []
        self.game_is_running = True
        self.valid_player_action = False
        self.player_is_acting = False


    def save_result(self):
        self.player_points = self.win_info['player_points']


    def play(self):
        Thread(target=self.relay).start()
        Thread(target=self.game.run).start()
        
        # set game info
        self.win_info = {'win':False, 'waiting_on_win':True, 'player_points':[]}
        # set game board
             #Game.game_setup_grafics
        self.sender.send(category='game', name='setup values', info={'function':Game.game_setup_values.__name__, 'parameter':''})
        self.sender.send(category='game', name='setup grafics', info={'function':Game.game_setup_grafics.__name__, 'parameter':''})
        # game course
        while self.game_is_running:
            # for every playerd
            for player in self.active_player:
                # waiting on responce about action validity
                while not self.valid_player_action:
                    if self.player_is_acting:
                        self.sender.send(category='game', name='player act', info={'function':Game.player_act.__name__, 'parameter':self.player_action['info']})
                        self.player_is_acting = False
                    sleep(0.1)
                    # allow to exit game
                    if not self.game_is_running:
                        return
                self.valid_player_action = False

                # waiting on responce about end of game
                self.sender.send(category='game', name=f'check win for player {player}', info={'function':Game.check_win.__name__, 'parameter':''})
                while self.win_info['waiting_on_win']:
                    sleep(0.1)
                if self.win_info['win']:
                    self.game_is_running = False
                    break
                self.win_info['waiting_on_win'] = True
        self.save_result()


    def relay(self):
        self.sender.add_listener(self.game.reseiver)
        self.game.sender.add_listener(self.reseiver)
        self.active_relay = True
        while self.active_relay:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "gui":
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                elif message['category'] == "input":
                    self.player_action = message
                    self.player_is_acting = True
                elif message['category'] == "action_validity":
                    self.valid_player_action = message['info']
                elif message['category'] == "win":
                    self.win_info = message['info']
                elif message['category'] in ["exit", "close_game"]:
                    if message['category'] == "exit":
                        self.interrupt_exit = True
                    self.sender.send(category=message['category'], name=message['name'], info=message['info'])
                    self.game_is_running = False
                    self.active_relay = False
        print("closing game relay thread")


    def stop_relay(self):
        self.active_relay = False


    def get_interupt_exit(self):
        return self.interrupt_exit

# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    print("this is the multiplayer file")