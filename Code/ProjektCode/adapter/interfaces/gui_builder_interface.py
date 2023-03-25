"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class GuiBuilder(ABC):
    @abstractmethod
    def run(self):
        pass

    def set_window_info(self, window_info):
        pass

    def set_window_elements(self, window_elements):
        pass

    def create_window(self):
        pass

    def clear_window(self):
        pass

    def terminate_window(self):
        pass
        
    def create_window_interaction_elements(self):
        pass

    def set_element_styles(self):
        pass

    def load_image_on_screen(self, game_element):
        pass

    def update_window(self):
        pass

    def check_events(self):
        pass