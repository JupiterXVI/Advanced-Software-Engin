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
from unittest.mock import Mock

from adapter import DatabaseAccess
from core_files import Account
from core_files import AccountList


class test_AccountList(unittest.TestCase):

    def test_get_accounts(self):
        #arrange
        self.mock_datamanager = Mock(spec=DatabaseAccess)
        self.account_list = AccountList(self.mock_datamanager)
        self.mock_datamanager.get_player_table.return_value = [
            (1, 'user1', 'pass1', 25, False),
            (2, 'user2', 'pass2', 30, True)
        ]

        #act
        self.account_list.get_accounts()

        #assert
        self.assertEqual(len(self.account_list.account), 2)
        self.assertEqual(self.account_list.account[0].player_id, 1)
        self.assertEqual(self.account_list.account[0].name, 'user1')
        self.assertEqual(self.account_list.account[1].player_id, 2)
        self.assertEqual(self.account_list.account[1].name, 'user2')


    def test_add_account(self):
        #arrange
        self.mock_datamanager = Mock(spec=DatabaseAccess)
        self.account_list = AccountList(self.mock_datamanager)
        self.mock_datamanager.last_added_account.return_value = 3

        #act
        self.account_list.add_account('user3', 'pass3', 35, True)

        #assert
        self.assertEqual(len(self.account_list.account), 1)
        self.assertEqual(self.account_list.account[0].player_id, 3)
        self.assertEqual(self.account_list.account[0].name, 'user3')


    def test_save_account_data(self):
        #arrange
        self.mock_datamanager = Mock(spec=DatabaseAccess)
        self.account_list = AccountList(self.mock_datamanager)
        mock_account = Mock(spec=Account)
        mock_account.player_id = 1
        mock_account.name = 'user1'
        mock_account.password = 'pass1'
        mock_account.age = 25
        mock_account.is_admin = False

        #act
        self.account_list.save_account_data(mock_account)
        #assert

        self.mock_datamanager.update_account.assert_called_once_with(1, 'user1', 'pass1', 25, False)
