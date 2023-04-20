"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod
from .generic_menu_interface import GenericMenu

# astablish all funktions which a database connector has to provide
class ManageMenu(GenericMenu):
    @abstractmethod
    def get_selected_account(self):
        pass

    @abstractmethod
    def set_to_save_account(self, should_save):
        pass