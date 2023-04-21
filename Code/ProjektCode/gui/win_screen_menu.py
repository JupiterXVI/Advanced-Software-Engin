"""
imports
"""
from adapter import GenericMenu
from gui import WinScreen, MenuActions
from communication import Sender, Reseiver


class WinScreenMenu(GenericMenu):
    """
    global variables
    """
    def __init__(self):
        self.account_list = []
        self.point_list = []
        self.player_score_elements = []
        self.sender = Sender()
        self.reseiver = Reseiver()
    

    """
    functions
    """
    def change_menu(self):
        print("open win screen")
        self.get_player_score()
        self.player_score_elements = WinScreen.window_elements + self.player_score_elements
        MenuActions.get_window_elements_on_screen(self.player_score_elements, self.sender)


    def run(self):
        print("start win screen")
        menu_in_use = True
        while menu_in_use:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == "input":
                    if self.check_menu_action(message['info']):
                        menu_in_use = False
                elif message['category'] == "exit":
                    menu_in_use = False
        self.player_score_elements = []
        print("close win screen")
                    
    
    def check_menu_action(self, action):
        event = MenuActions.get_button_from_position(WinScreen.window_elements, action)
        if event == "start_menu":
            return True
        return False


    def get_player_score(self):
        account_index = 0
        for account in self.account_list:
            player = WinScreen.player_list[account_index]
            player['text']['content'] = account.get_name()
            points = WinScreen.points_list[account_index]
            points['text']['content'] = str(self.point_list[account_index])
            self.player_score_elements.append(player)
            self.player_score_elements.append(points)
            account_index += 1 
            

    def set_account_list(self, account_list):
        self.account_list = account_list


    def set_point_list(self, point_list):
        self.point_list = point_list
