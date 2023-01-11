"""
imports
"""
from adapter import MenuBuilder
from adapter import PostgreSqlAdapter
from adapter import Timer
#from core_files import Account
from core_files import AccountList
from gui import GameLibraryMenu
from gui import ChooseGameMenu
from gui import ManageAccountMenu

import pathlib


class Main():
    """
    global variables
    """
    def __init__(self):
        pass

    """
    functions
    """
    def test_database():
        print(PostgreSqlAdapter().get_player_table())

    def start():
        print("started main file...")
        timer = Timer()
        gui_builder = MenuBuilder()
        choose_game_menu = ChooseGameMenu(gui_builder, timer)
        account_list = AccountList(PostgreSqlAdapter())
        account_list.get_accounts()
        manage_account_menu = ManageAccountMenu(gui_builder, timer, account_list)
        library_menu = GameLibraryMenu(gui_builder, choose_game_menu, manage_account_menu, timer)
        library_menu.open_menu()
        library_menu.run_menu()

    def test():
        print(pathlib.Path.cwd().parent)


if __name__ == "__main__":
    # Main.test_database()
    Main.start()