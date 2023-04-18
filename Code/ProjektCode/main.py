"""
imports
"""
from adapter import PygameBuilder, PostgreSqlAdapter
from core_files import AccountList, Playground, Singleplayer, Multiplayer, GameList, Statistics
from gui import StartMenu, ChooseGameMenu, AccountSelectionMenu, WinScreenMenu, ManageAccountMenu, EditAccountMenu, MenuManager
from games import TicTacToe 

from threading import Thread


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

        # start up gui plugin
        gui_builder = PygameBuilder()
        Thread(target=gui_builder.run).start()

        # create menu instances and sync with data from database
        st_menu = StartMenu()

        cg_menu = ChooseGameMenu()

        ma_menu = ManageAccountMenu()
        ac_list = AccountList(PostgreSqlAdapter())
        ac_list.get_accounts()
        ma_menu.set_account_list(ac_list)

        ea_menu = EditAccountMenu()

        as_menu = AccountSelectionMenu(ac_list)

        ws_menu = WinScreenMenu()

        stats = Statistics(PostgreSqlAdapter())
        stats.get_statistics()

        # add all games to a list and make them playable through the playground
        game_list = GameList(PostgreSqlAdapter())
        game_list.add_game(TicTacToe())
        s_player = Singleplayer()
        m_player = Multiplayer()
        playground = Playground(game_list.games, gui_builder, s_player, m_player)
        
        playground.set_select_screen(as_menu)
        playground.set_win_screen(ws_menu)
        playground.set_statistics(stats)

        # connect menus and start up menu interaction
        menus = MenuManager(gui_builder, st_menu, cg_menu, ma_menu, ea_menu)
        Thread(target=menus.run_relay).start()

        # open gui window
        menus.setup_window()

        # open up main menu
        # open menu after game closes
        while menus.should_come_back_to_menu():
            menus.open_menus()

            stats.get_statistics()

            game = cg_menu.get_chousen_game()
            
            # select the chousen game
            if game != "no game chousen":    
                game_index = 0
                for games in game_list.games:
                    if games.get_name() == game:
                        break 
                    game_index += 1
                if game_index < len(game_list.games):
                    # play the selected game
                    playground.play(game_id = game_index)
                else:
                    print(f"{game} is currently not available")
                # allow for different game to be chousen
                cg_menu.set_chousen_game("no game chousen")

        print("end")


if __name__ == "__main__":
    Main.start()
