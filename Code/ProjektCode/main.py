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
        """
        # creat a Window
        gui_builder = MenuBuilder()
        gui_builder.set_window_info(ChooseGraphicTTT.tic_tac_toe_window)
        gui_builder.create_window()
        """
        # get TicTacToe in playground
        game_list = GameList(PostgreSqlAdapter())
        game_list.add_game(TicTacToe())
        playground = Playground(game_list.games)
        #start game
        playground.play(game_id = 1 -1)

    def test_messaging():
        window_open = "not Initialized"
        main_sender = Sender()
        main_reseiver = Reseiver()
        gui_builder = PygameBuilder()
        main_sender.add_listener(gui_builder.reseiver)
        gui_builder.sender.add_listener(main_reseiver)
        Thread(target=gui_builder.run).start()

        main_sender.send(category='gui',name='send_window_info', info={'function':GuiBuilder.set_window_info.__name__, 'parameter':MainMenu.window})
        main_sender.send(category='gui', name='send_element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':MainMenu.window_elements})
        main_sender.send(category='gui', name='create_window', info={'function':GuiBuilder.create_window.__name__, 'parameter':''})
        window_open = True
        
        ttt = TicTacToe()
        main_sender.add_listener(ttt.reseiver)
        ttt.sender.add_listener(gui_builder.reseiver)
        Thread(target=ttt.run).start()
        
        main_sender.send(category='game', name='draw_board', info={'function':'draw_board', 'parameter':''})
        main_sender.send(category='game', name='draw_board', info={'function':'draw_board', 'parameter':''})

        while window_open:
            if main_reseiver.event_reseved:
                message = main_reseiver.get_message()
                print(message)

                if message['category'] == 'input':
                    main_sender.send(category='game', name='position', info={'function':'position_active_symbol', 'parameter':message['info']})
                    main_sender.send(category='game', name='symboles', info={'function':'draw_symbols', 'parameter':''})
                    main_sender.send(category='game', name='change_player', info={'function':'change_symbols', 'parameter':''})
                    main_sender.send(category='game', name='check_win', info={'function':'check_win', 'parameter':''})

        # muss mit Mülleimer geschlossen werden

    def message_relay(self):
        pass


if __name__ == "__main__":
    # Main.test()
    # Main.start()
    Main.test_messaging()
