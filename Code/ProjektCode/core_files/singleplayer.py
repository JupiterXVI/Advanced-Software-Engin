"""
imports
"""
#from game import Game
from communication import Sender, Reseiver


class Singleplayer():
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

    def get_active_player(self):
        return [self.active_player]
    

    def get_points(self):
        return [self.player_points]
    

    def play(self):
        pass


    def add_player(self, new_player):
        self.active_player.append(new_player)
        self.player_points.append(0)


    def reset_player(self):
        self.active_player = []
        self.player_points = []
        

    def player_act(self):
        print("singleplayer action")


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
    print("this is the singleplayer file")
