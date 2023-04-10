"""
Interfaces zur Estellung eines Beobachters
"""
from abc import ABC, abstractmethod


class Listener(ABC):
    @abstractmethod
    def listen(self, send_event): 
        pass