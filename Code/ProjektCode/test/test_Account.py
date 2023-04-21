"""
1. Werden Werte eines Accounts richtig ausgegeben?
2. Kann das Alter eines Accounts geändert werden?
3. Kann das Passwort eines Accounts geändert werden?
4. Können Werte von Account aktualisiert werden?
"""
"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

import unittest
from core_files import Account


class test_Account(unittest.TestCase):

    def test_get_values(self):
        #arrange
        account = Account(2, "name", "password", 15, 0)
        #act
        id = account.get_id()
        #assert
        self.assertEqual(id, 2)


    def test_set_age(self):
        self.account = Account(2, "name", "password", 15, 0)
        self.account.set_age(30)
        self.assertEqual(self.account.age, 30)


    def test_set_password(self):
        self.account = Account(2, "name", "password", 15, 0)
        self.account.set_password("newpassword")
        self.assertEqual(self.account.password, "newpassword")
