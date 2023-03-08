"""
imports
"""
from adapter import MenuBuilder
from adapter import PostgreSqlAdapter
from core_files import AccountList  

from gui import GameLibraryMenu
from gui import ChooseGameMenu
from gui import ManageAccountMenu

from core_files import Playground
from core_files import GameList
from games import TicTacToe
from games import ChooseGraphicTTT


class Main():
    """
    global variables
    """
    def __init__(self):
        pass

    """
    functions
    """
    def start():
        print("started main file...")
        gui_builder = MenuBuilder()
        account_list = AccountList(PostgreSqlAdapter())
        account_list.get_accounts()
        choose_game_menu = ChooseGameMenu(gui_builder)
        manage_account_menu = ManageAccountMenu(gui_builder, account_list)
        library_menu = GameLibraryMenu(gui_builder, choose_game_menu, manage_account_menu)
        library_menu.open_menu()
        library_menu.run_menu()

    def test():
        # creat a Window
        gui_builder = MenuBuilder()
        gui_builder.set_window_info(ChooseGraphicTTT.tic_tac_toe_window)
        gui_builder.create_window()
        # get TicTacToe in playground
        game_list = GameList([TicTacToe()], PostgreSqlAdapter())
        playground = Playground(game_list.games, gui_builder)
        #start game
        playground.play(game_id = 1 -1)


if __name__ == "__main__":
    Main.test()
    # Main.start()
