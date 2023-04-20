"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


# astablish all funktions which a database connector has to provide
class GenericMenu(ABC):
    @abstractmethod
    def change_menu(self):
        pass
    
    
    @abstractmethod
    def run(self):
        pass