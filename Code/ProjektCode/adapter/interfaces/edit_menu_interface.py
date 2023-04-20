"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod
from .generic_menu_interface import GenericMenu

# astablish all funktions which a database connector has to provide
class EditMenu(GenericMenu):
    @abstractmethod
    def get_to_save_account(self):
        pass

    @abstractmethod
    def set_account(self, account):
        pass