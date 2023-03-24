"""
imports
"""
from sys import exit

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
        window_open = "not Initialized"
        main_sender = Sender()
        main_resever = Resiver()
        gui_builder = MenuBuilder()
        main_sender.add_listener(gui_builder.resiver)
        gui_builder.sender.add_listener(main_resever)
        Thread(target=gui_builder.run).start()

        main_sender.set_event(category='gui',name='send_window_info', info={'function':'set_window_info', 'parameter':MainMenu.window})
        main_sender.send()
        
        main_sender.set_event(category='gui', name='send_element_info', info={'function':'set_window_elements', 'parameter':MainMenu.window_elements})
        main_sender.send()
    
        main_sender.set_event(category='gui', name='create_window', info={'function':'create_window', 'parameter':''})
        main_sender.send()
        window_open = True
        
        ttt = TicTacToe()
        main_sender.add_listener(ttt.resiver)
        ttt.sender.add_listener(gui_builder.resiver)
        Thread(target=ttt.run).start()
        
        main_sender.set_event(category='game', name='draw_board', info={'function':'draw_board', 'parameter':''})
        main_sender.send()

        main_sender.set_event(category='game', name='draw_board', info={'function':'draw_board', 'parameter':''})
        main_sender.send()

        #main_sender.set_event(category='gui', name='show_board', info={'function':'update_window', 'parameter':''})
        #main_sender.send() 

        """
        main_sender.set_event(category='gui', name='create_interaction', info={'function':'create_window_interaction_elements', 'parameter':''})
        main_sender.send()
        
        main_sender.set_event(category='gui', name='modifie_element_style', info={'function':'set_element_styles', 'parameter':''})
        main_sender.send()
        
        main_sender.set_event(category='gui', name='show_elements_on _window', info={'function':'update_window', 'parameter':''})
        main_sender.send()
        print("wait on main menu")
        #sleep(2)

        #main_sender.set_event(category='gui', name='clear_screen', info={'function':'clear_window', 'parameter':''})
        #main_sender.send()
        #sleep(1)
        """

        while window_open:
            if main_resever.event_reseved:
                message = main_resever.get_message()
                print(message)

                if message['category'] == 'input':
                    main_sender.set_event(category='game', name='position', info={'function':'position_active_symbol', 'parameter':message['info']})
                    main_sender.send()
                    main_sender.set_event(category='game', name='symboles', info={'function':'draw_symbols', 'parameter':''})
                    main_sender.send()
                    main_sender.set_event(category='game', name='change_player', info={'function':'change_symbols', 'parameter':''})
                    main_sender.send()
                    main_sender.set_event(category='game', name='check_win', info={'function':'check_win', 'parameter':''})
                    main_sender.send()

        # muss mit Mülleimer geschlossen werden

    def message_relay(self):
        pass


if __name__ == "__main__":
    # Main.test()
    # Main.start()
    Main.test_messaging()
