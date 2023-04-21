"""
Interface to further specify menu behavior
"""
from abc import ABC, abstractmethod
from .generic_menu_interface import GenericMenu

class EditMenu(GenericMenu):
    @abstractmethod
    def get_to_save_account(self):
        pass

    @abstractmethod
    def set_account(self, account):
        pass
    