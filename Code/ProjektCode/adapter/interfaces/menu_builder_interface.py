"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class AllowToBuldMenu(ABC):
    @abstractmethod
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

    def update_window(self):
        pass

    def check_events(self):
        pass