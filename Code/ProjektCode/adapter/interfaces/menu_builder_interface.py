"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class AllowToBuldMenu(ABC):
    @abstractmethod
    def set_window_info(self, window_info):
        pass

    def set_window_elements(self, window_elements):
        pass

    def set_game_elements(self, game_elements):
        pass

    def create_window(self):
        pass

    def clear_window(self):
        pass

    def terminate_window(self):
        pass
        
    def create_window_interaction_elements(self):
        pass

    def set_element_styles(self):
        pass

    def create_game_elements(self):
        pass

    def set_game_element_styles(self):
        pass

    def update_window(self):
        pass

    def check_events(self):
        pass