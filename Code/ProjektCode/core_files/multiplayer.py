"""
imports
"""
from adapter import GuiBuilder
from core_files import Game
from communication import Sender, Reseiver
from threading import Thread
from time import sleep

# AUSLAGERN - Erstellen des Fensters
from gui import MainMenu

class Multiplayer():
    """
    global variables
    """
    def __init__(self, game):
        self.game = game
        self.active_player = []
        self.player_points = []
        self.win_info = "not set"
        self.game_is_running = True
        self.valid_player_action = False
        self.player_is_acting = False
        self.player_action = "no player action"
        self.sender = Sender()
        self.reseiver = Reseiver()

    """
    functions
    """
    def select_player(self):
        for player in range(self.game.player_count):
            print("select player in menu screen")
            # select screen
            self.add_player(f"Dummy_Player{player}")


    def add_player(self, new_player):
        self.active_player.append(new_player)
        self.player_points.append(0)


    def show_result(self):
        # show result screen
        self.player_points = self.win_info['player_points']
        index = 0
        for player in self.active_player:
            print(f"{player} gets {self.player_points[index]} points")
            index += 1


    def play(self):
        Thread(target=self.relay).start()
        Thread(target=self.game.run).start()
        self.select_player()
        # AUSLAGERN - Estellen des Fensters
        self.sender.send(category='gui',name='send_window_info', info={'function':GuiBuilder.set_window_info.__name__, 'parameter':MainMenu.window})
        self.sender.send(category='gui', name='send_element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':MainMenu.window_elements})
        self.sender.send(category='gui', name='create_window', info={'function':GuiBuilder.create_window.__name__, 'parameter':''})
        
        # set game info
        self.win_info = {'win':False, 'waiting_on_win':True, 'player_points':[]}
        # set game board
        self.sender.send(category='game', name='setup values', info={'function':'game_setup_values', 'parameter':''})
        self.sender.send(category='game', name='setup grafics', info={'function':'game_setup_grafics', 'parameter':''})
        # game course
        while self.game_is_running:
            # for every playerd
            for player in self.active_player:
                # waiting on responce about action validity
                while not self.valid_player_action:
                    if self.player_is_acting:
                        print(f"player{player} is acting")
                        self.sender.send(category='game', name='player act', info={'function':Game.player_act.__name__, 'parameter':self.player_action['info']})
                        self.player_is_acting = False
                    sleep(0.1)
                self.valid_player_action = False

                # waiting on responce about end of game
                self.sender.send(category='game', name=f'check win for player {player}', info={'function':Game.check_win.__name__, 'parameter':''})
                while self.win_info['waiting_on_win']:
                    sleep(0.1)
                if self.win_info['win']:
                    self.game_is_running = False
                    break
                self.win_info['waiting_on_win'] = True
        self.show_result()
        

    def relay(self):
        self.sender.add_listener(self.game.reseiver)
        self.game.sender.add_listener(self.reseiver)
        while True:
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


# führe nur aus wenn die Datei direckt ausgeführt wird
if __name__ == "__main__":
    print("this is the multiplayer file")