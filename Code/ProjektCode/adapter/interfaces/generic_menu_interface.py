"""
Interface to specify menu behavior
"""
from abc import ABC, abstractmethod


class GenericMenu(ABC):
    @abstractmethod
    def change_menu(self):
        pass
    
    
    @abstractmethod
    def run(self):
        pass
