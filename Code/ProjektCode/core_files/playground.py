"""
imports
"""
from adapter import GuiBuilder
from core_files import Singleplayer, Multiplayer
from communication import Sender, Reseiver
from gui import AccountSelectionMenu

from core_files import AccountList
from adapter import PostgreSqlAdapter


class Playground():
    """
    global variables
    """
    def __init__(self, game_list, gui:GuiBuilder, s_player:Singleplayer, m_player:Multiplayer):
        self.game_list = game_list
        self.gui = gui
        self.s_player = s_player
        self.m_player = m_player
        self.select_screen = "not set"
        self.win_screen = "not set"
        self.statistics = "not set"
        self.sender = Sender()
        self.resiever = Reseiver()


    """
    functions
    """
    def play(self, game_id):
        game = self.game_list[game_id]
        play_pattern = self.choose_play_pattern(game)
        if play_pattern == "no pattern set":
            return
        play_pattern.reseiver.empty_message_queue()
        play_pattern.play()
        self.clean_up(play_pattern)
        self.remove_from_gui(play_pattern)
        if play_pattern.was_exited_by_interrupt():
            return
        self.save_results(play_pattern)
        self.show_results(play_pattern)
        play_pattern.reset_game()


    def set_select_screen(self, screen):
        self.select_screen = screen


    def set_win_screen(self, screen):
        self.win_screen = screen

    def set_statistics(self, statistics):
        self.statistics = statistics

    def connect_to_gui(self, element):
        element.sender.add_listener(self.gui.reseiver)
        self.gui.sender.add_listener(element.reseiver)

    
    def remove_from_gui(self, element):
        element.sender.remove_listener(self.gui.reseiver)
        self.gui.sender.remove_listener(element.reseiver)


    def clean_up(self, play_pattern):
        play_pattern.sender.send(category='close_game', name='close game', info={'function':'', 'parameter':''})
        play_pattern.stop_relay()
    

    def choose_play_pattern(self, game):
        play_pattern = "no pattern set"
        if game.get_player_count() > 1:
            self.m_player.set_game(game)
            play_pattern = self.m_player
            self.connect_to_gui(play_pattern)
            for user in range(game.player_count):
                if not self.add_player_to_pattern(play_pattern):
                    return "no pattern set"
        else:
            self.s_player.set_game(game)
            play_pattern = self.s_player
            self.connect_to_gui(play_pattern)
            if not self.add_player_to_pattern(play_pattern):
                return "no pattern set"
        return play_pattern


    def add_player_to_pattern(self, play_pattern):
        player = self.choose_player()
        if player == "not set":
                return False
        play_pattern.add_player(player)
        return True
        

    def choose_player(self):
        try:
            self.connect_to_gui(self.select_screen)
            self.select_screen.change_menu()
            self.select_screen.run()
            self.remove_from_gui(self.select_screen)
        except:
            print("select screen cam't be opend")
        return self.select_screen.get_selection()
    

    def save_results(self, play_pattern):
        if self.statistics == "not set":
            return
        game = play_pattern.get_game()
        points = play_pattern.get_points()
        player_index = 0
        for player in play_pattern.get_active_player():
            if points[player_index] > 0:
                self.statistics.increase_wins(player.get_id(), game.get_id())
            else:
                self.statistics.increase_losses(player.get_id(), game.get_id())
            player_index += 1
    

    def show_results(self, play_pattern):
        self.win_screen.set_account_list(play_pattern.get_active_player())
        self.win_screen.set_point_list(play_pattern.get_points())
        self.connect_to_gui(self.win_screen)
        self.win_screen.change_menu()
        self.win_screen.run()
        self.remove_from_gui(self.win_screen)
