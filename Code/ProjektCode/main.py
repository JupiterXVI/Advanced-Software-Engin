"""
imports
"""
from adapter import MenuBuilder
from adapter import PostgreSqlAdapter
from adapter import Timer
from core_files import Account
from gui import GameLibraryMenu
from gui import MainMenu


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
        player1 = Account(3, 'Bob', 'changeme', '15', False, PostgreSqlAdapter())
        print(PostgreSqlAdapter().get_player_table())
        player1.set_age(5)
        player1.save_account_data()
        print(PostgreSqlAdapter().get_player_table())

    def start():
        print("started main file...")
        timer = Timer()
        main_menu = MenuBuilder(MainMenu.window, MainMenu.window_elements)
        library = GameLibraryMenu(main_menu)
        library.open_main_menu()
        library.run_main_menu(timer)

if __name__ == "__main__":
    Main.test_database()
    Main.start()