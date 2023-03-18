"""
imports
"""
from adapter import MenuBuilder, PostgreSqlAdapter
from core_files import AccountList, Playground, GameList
from gui import GameLibraryMenu, MainMenu, ChooseGameMenu, ManageAccountMenu
from games import TicTacToe, ChooseGraphicTTT

from time import sleep
from threading import Thread
from communication import Sender, Resiver


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

    def test_messaging():
        main_sender = Sender()
        main_resever = Resiver()
        gui_builder = MenuBuilder()

        main_sender.add_listener(gui_builder.resiver)
        gui_builder.sender.add_listener(main_resever)

        Thread(target=gui_builder.run).start()
        sleep(3)

        main_sender.set_event('send_window_info', {'function':'set_window_info', 'parameter':MainMenu.window})
        main_sender.send()
        sleep(1)

        main_sender.set_event('send_element_info', {'function':'set_window_elements', 'parameter':MainMenu.window_elements})
        main_sender.send()
        sleep(1)
        
        main_sender.set_event('create_window', {'function':'create_window', 'parameter':''})
        main_sender.send()
        sleep(1)

        main_sender.set_event('create_interaction', {'function':'create_window_interaction_elements', 'parameter':''})
        main_sender.send()
        sleep(1)

        main_sender.set_event('modifie_element_style', {'function':'set_element_styles', 'parameter':''})
        main_sender.send()
        sleep(1)

        main_sender.set_event('show_elements_on _window', {'function':'update_window', 'parameter':''})
        main_sender.send()
        
        print("done")



if __name__ == "__main__":
    # Main.test()
    Main.start()
    # Main.test_messaging()
