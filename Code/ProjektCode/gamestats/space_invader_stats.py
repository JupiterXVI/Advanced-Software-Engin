"""
imports
"""
import os
import sys
sys.path.append(os.path.join(sys.path[0], '..'))
from core_files.statistic import Statistic


class SpaceInvaderStats(Statistic):
    """
    global variables
    """
    def __init__(self, game_id, player_id):
        super().__init__(game_id, player_id)

    """
    functions
    """