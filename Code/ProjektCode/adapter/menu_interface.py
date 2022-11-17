"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class AllowToBuldMenu(ABC):
    @abstractmethod
    def create_window(self):
        pass
        
    def create_window_elements(self):
        pass

    def set_styles(self):
        pass