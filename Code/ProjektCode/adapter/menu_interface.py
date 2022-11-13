"""
Interfaces zur Estellung eines Menüs
"""

from abc import ABC, abstractmethod

class Clickable(ABC):
    @abstractmethod
    def on_click(self):
        pass

class Showable(ABC):
    @abstractmethod
    def show(self):
        pass

class AllowToBuldMenu(ABC):
    @abstractmethod
    def create_window(self):
        pass
        
    def create_buttons(self):
        pass

    def set_styles(self):
        pass