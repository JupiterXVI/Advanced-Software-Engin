"""
1. Testen, ob Attribute der Klasse "Statistic" beim Erstellen korrekt gesetzt werden
2. Werden "wins"-Attribute aktualisiert?
3. Werden "Losses"-Attribute aktualisiert?
"""
"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from core_files import Statistics
from adapter import DatabaseAccess
from core_files import GameStatistic

import unittest
from unittest.mock import MagicMock


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # arrange 
        self.database_access = MagicMock(spec=DatabaseAccess)
        self.stats = Statistics(self.database_access)
        self.stats.player_game_stats = [
            GameStatistic(1, 1, 3, 2),
            GameStatistic(2, 1, 1, 5),
            GameStatistic(1, 2, 2, 4)
        ]
    
    def test_get_statistics(self):
        # arrange 
        self.database_access.get_game_stat_table.return_value = [
            (1, 1, 3, 2),
            (2, 1, 1, 5),
            (1, 2, 2, 4)
        ]

        # act
        self.stats.get_statistics()
        
        # assert
        self.assertEqual(len(self.stats.player_game_stats), 3)
    
    def test_increase_wins(self):
        # arrange 
        self.database_access.add_win.return_value = None
        
        # act
        self.stats.increase_wins(1, 1)
        
        # assert
        self.assertEqual(self.stats.player_game_stats[0].get_wins(), 4)
    
    def test_increase_losses(self):
        # arrange 
        self.database_access.add_loss.return_value = None
        
        # act
        self.stats.increase_losses(1, 1)
        
        # assert
        self.assertEqual(self.stats.player_game_stats[0].get_losses(), 3)

   
        
        