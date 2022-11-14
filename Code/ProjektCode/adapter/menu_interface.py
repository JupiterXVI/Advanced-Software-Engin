"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class AllowToBuldMenu(ABC):
    @abstractmethod
    def create_window(self):
        pass
        
    def create_buttons(self):
        pass

    def set_styles(self):
        pass