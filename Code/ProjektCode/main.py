"""
imports
"""
from threading import Thread

from adapter import PygameBuilder, PostgreSqlAdapter
from core_files import AccountList, Playground, GameList
from gui import MenuManager, GameLibraryMenu, ChooseGameMenu, ManageAccountMenu, EditAccountMenu
from games import TicTacToe



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

        # add all games to a list and make them playable through the playground
        game_list = GameList(PostgreSqlAdapter())
        game_list.add_game(TicTacToe())
        playground = Playground(game_list.games, gui_builder)

        # connect menus and start up menu interaction
        gl_menu = GameLibraryMenu()

        cg_menu = ChooseGameMenu()

        ma_menu = ManageAccountMenu()
        ac_list = AccountList(PostgreSqlAdapter())
        ac_list.get_accounts()
        ma_menu.set_account_list(ac_list)
        
        ea_menu = EditAccountMenu()

        menus = MenuManager(gui_builder, gl_menu, cg_menu, ma_menu, ea_menu)
        Thread(target=menus.run_relay).start()

        # open gui window
        menus.setup_window()

        # open up main menu
        # open menu after game closes
        while menus.should_come_back_to_menu():
            menus.open_menus()
            game = cg_menu.get_chousen_game()
            
            # select the chousen game
            if game != "no game chousen":    
                game_index = 0
                for games in game_list.games:
                    if games.get_name() == game:
                        break 
                    game_index += 1
                # play the selected game
                playground.play(game_id = game_index)
                # allow for different game to be chousen
                cg_menu.set_chousen_game("no game chousen")

        print("end")




if __name__ == "__main__":
    Main.start()
