"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class GuiBuilder(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def set_window_info(self, window_info):
        pass

    @abstractmethod
    def set_window_elements(self, window_elements):
        pass

    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def clear_window(self):
        pass

    @abstractmethod
    def terminate_window(self):
        pass
        
    @abstractmethod
    def create_window_interaction_elements(self):
        pass

    @abstractmethod
    def set_element_styles(self):
        pass

    @abstractmethod
    def load_image_on_screen(self, game_element):
        pass

    @abstractmethod
    def update_window(self):
        pass

    @abstractmethod
    def check_events(self):
        pass