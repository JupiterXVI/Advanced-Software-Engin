"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def open_menu(self):
        pass

    def run_menu(self):
        pass
    
    def close_menu(self):
        pass