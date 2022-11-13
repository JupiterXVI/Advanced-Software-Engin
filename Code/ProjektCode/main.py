from core_files import Account
from adapter import get_connection
from core_files import GameLibrary
from gui import Menu


def test_from_import_core_files():
    a = Account(1, "Tim", "timpw", "14", False)
    print(a.get_name())

def test_from_import_adapter():
    get_connection()

if __name__ == "__main__":
    print("started main file...")
    #test_from_import_core_files()
    #test_from_import_adapter()
    menu = Menu(600, 600)
    library = GameLibrary(menu)
    library.open_main_menu()
