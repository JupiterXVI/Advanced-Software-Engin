"""
imports
"""
from adapter import PygameBuilder, PostgreSqlAdapter
from core_files import AccountList, Playground, GameList
from gui import GameLibraryMenu, ChooseGameMenu, ManageAccountMenu, EditAccountMenu
from games import TicTacToe

from threading import Thread

from gui import MenuManager

from gui import Window
# from gui import Window

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


    def test_game():
        gui_builder = PygameBuilder()
        Thread(target=gui_builder.run).start()
        # get TicTacToe in playground
        game_list = GameList(PostgreSqlAdapter())
        game_list.add_game(TicTacToe())
        playground = Playground(game_list.games, gui_builder)
        #start game
        playground.play(game_id = 1 -1)
        print("end game")


    def test_menu():
        gui_builder = PygameBuilder()
        Thread(target=gui_builder.run).start()

        gl_menu = GameLibraryMenu()
        cg_menu = ChooseGameMenu()
        ma_menu = ManageAccountMenu()
        ea_menu = EditAccountMenu()

        # get TicTacToe in playground
        menus = MenuManager(gui_builder, gl_menu, cg_menu, ma_menu, ea_menu)
        Thread(target=menus.run_relay).start()
        menus.setup_window(Window)
        menus.open_menus()
        print("end")


if __name__ == "__main__":
    # Main.test_game()
    Main.test_menu()
    
    # Main.start()
