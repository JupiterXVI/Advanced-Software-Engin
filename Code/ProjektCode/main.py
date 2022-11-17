from core_files import Account
from core_files import GameLibrary
from adapter import get_connection
from gui import Menu


def test_from_import_core_files():
    a = Account(1, "Tim", "timpw", "14", False)
    print(a.get_name())

def test_from_import_adapter():
    get_connection()



print("started main file...")
menu = Menu(600, 600)
library = GameLibrary(menu)
library.open_main_menu()
#test_from_import_core_files()
#test_from_import_adapter()