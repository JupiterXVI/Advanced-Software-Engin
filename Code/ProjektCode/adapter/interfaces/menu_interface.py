"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod

class Menu(ABC):
    # 50 FPS
    allow_passes_per_second =  0.02
    # wait after click option
    blocking_wait_seconds =  0.3

    @abstractmethod
    def open_menu(self):
        pass

    def run_menu(self):
        pass
    
    def close_menu(self):
        pass