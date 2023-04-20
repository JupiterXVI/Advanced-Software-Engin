"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod

# astablish all funktions which a database connector has to provide
class Manager():
    @abstractmethod
    def setup_window(self):
        pass

    @abstractmethod
    def open_menus(self):
        pass

    @abstractmethod
    def should_come_back_to_menu(self):
        pass

    @abstractmethod
    def run_relay(self):
        pass