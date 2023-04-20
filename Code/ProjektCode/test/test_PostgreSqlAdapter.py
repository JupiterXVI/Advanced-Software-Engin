"""
1. Testen, ob config ein dictionary zurückgibt
2. Können neue Accounts erstellt werden?
3. Können bestehende Accounts gbearbeitet werden?
4. Ist das Löschen von Accounts möglich?
5. Werden das Tuple eines Accounts richtig ausgegeben?
"""
"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

#import coverage
import unittest
from adapter import PostgreSqlAdapter


class test_PostgreSqlAdapter(unittest.TestCase):
    def test_config(self):
        #arrange
        self.adapter = PostgreSqlAdapter()
        #act
        result = self.adapter.config()
        #assert
        self.assertIsInstance(result, dict)

    def test_add_account(self):
        self.adapter = PostgreSqlAdapter()
        result = len(self.adapter.get_player_table())
        self.adapter.add_account('test_addaccount', 'password', 25, False)
        self.assertIsInstance(result, int)
        self.assertEqual(result + 1, len(self.adapter.get_player_table()))
        #undo changes
        self.adapter.delete_account(self.adapter.last_added_account())

    def test_update_account(self):
        self.adapter = PostgreSqlAdapter()
        self.adapter.get_player(1)
        self.adapter.update_account(1, 'new_test', 'new_test', '30', True)
        result = self.adapter.get_player(1)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[1], 'new_test')
        self.assertEqual(result[2], 'new_test')
        self.assertEqual(result[3], '30')
        self.assertEqual(result[4], True)
        #undo changes
        self.adapter = PostgreSqlAdapter()
        self.adapter.get_player(1)
        self.adapter.update_account(1, 'test', 'test', '20', False)

    def test_delete_account(self):
        self.adapter = PostgreSqlAdapter()
        result1 = self.adapter.get_player_table()
        self.adapter.add_account('test_delete', 'test_delete', 25, False)
        self.adapter.delete_account(self.adapter.last_added_account())
        result2 = self.adapter.get_player_table()
        self.assertEqual(len(result1), len(result2))

    def test_get_player(self):
        self.adapter = PostgreSqlAdapter()
        self.adapter.add_account('admin', 'admin', '99', True)
        result = self.adapter.get_player(0)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 'admin')
        self.assertEqual(result[2], 'admin')
        self.assertEqual(result[3], '99')
        self.assertEqual(result[4], True)
