"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

import unittest
from adapter import PostgreSqlAdapter
from unittest.mock import patch, MagicMock


class TestPostgreSqlAdapter(unittest.TestCase):
    
    def setUp(self):
        self.adapter = PostgreSqlAdapter()

    @patch('adapter.PostgreSqlAdapter.get_connection')
    def test_add_account(self, mock_get_connection):
        # arrange
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cur)
        
        # act
        self.adapter.add_account('test_user', 'test_password', 18, False)

        # assert
        mock_conn.commit.assert_called_once()
        mock_cur.execute.assert_called_once_with(
            "INSERT INTO player(username, password, age, is_admin) VALUES(%s, %s, %s, %s);", 
            ('test_user', 'test_password', 18, False)
        )


    @patch('adapter.PostgreSqlAdapter.get_connection')
    def test_add_account_gamestats(self, mock_get_connection):
        # arrange
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cur)
        mock_cur.fetchone.return_value = (3,0)  # game count

        # act
        self.adapter.add_account_gamestats(1)

        # assert
        mock_conn.commit.assert_called_once()
        mock_cur.execute.assert_called_with(
            "INSERT INTO gamestats(fk_player_id, fk_game_id, wins, losses) VALUES(%s, %s, %s, %s);",
            (1, 3, 0, 0)
        )
        self.assertEqual(mock_cur.execute.call_count, 4)


    @patch('adapter.PostgreSqlAdapter.get_connection')
    def test_last_added_account(self, mock_get_connection):
        # arrange
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_cur.fetchone.return_value = (5,0)
        mock_get_connection.return_value = (mock_conn, mock_cur)

        # act
        result = self.adapter.last_added_account()

        # assert
        mock_cur.execute.assert_called_once_with('SELECT MAX(player_id) FROM player')
        self.assertEqual(result, 5)


    @patch('adapter.PostgreSqlAdapter.get_connection')
    def test_update_account(self, mock_get_connection):
        # arrange
        mock_conn = MagicMock()
        mock_cur = MagicMock()
        mock_get_connection.return_value = (mock_conn, mock_cur)

        # act
        self.adapter.update_account(1, 'test_user', 'test_password', 18, False)

        # assert
        mock_conn.commit.assert_called_once()
        mock_cur.execute.assert_called_once_with(
            "UPDATE player SET username = %s, password = %s, age = %s, is_admin = %s WHERE player_id = %s;",
            ('test_user', 'test_password', 18, False, 1)
        )