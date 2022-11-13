from core_files.account import Account
from adapter import get_connection

def test_from_import_core_files():
    a = Account(1, "Tim", "timpw", "14", False)
    print(a.get_name())

def test_from_import_adapter():
    get_connection()

if __name__ == "__main__":
    print("started main file...")
    test_from_import_core_files()
    test_from_import_adapter()