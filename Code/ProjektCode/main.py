"""
imports
"""
from adapter import PygameBuilder, GuiBuilder, PostgreSqlAdapter
from core_files import AccountList, Playground, GameList
from gui import GameLibraryMenu, MainMenu, ChooseGameMenu, ManageAccountMenu
from games import TicTacToe, ChooseGraphicTTT

from threading import Thread
from communication import Sender, Reseiver


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
        gui_builder = PygameBuilder()
        account_list = AccountList(PostgreSqlAdapter())
        account_list.get_accounts()
        choose_game_menu = ChooseGameMenu(gui_builder)
        manage_account_menu = ManageAccountMenu(gui_builder, account_list)
        library_menu = GameLibraryMenu(gui_builder, choose_game_menu, manage_account_menu)
        library_menu.open_menu()
        library_menu.run_menu()


    def test():
        gui_builder = PygameBuilder()
        Thread(target=gui_builder.run).start()
        # get TicTacToe in playground
        game_list = GameList(PostgreSqlAdapter())
        game_list.add_game(TicTacToe())
        playground = Playground(game_list.games, gui_builder)
        #start game
        playground.play(game_id = 1 -1)
        print("end game")


if __name__ == "__main__":
    Main.test()
    # Main.start()
