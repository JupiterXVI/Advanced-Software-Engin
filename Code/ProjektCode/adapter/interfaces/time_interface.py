"""
Interfaces zur Estellung eines Menüs
"""
from abc import ABC, abstractmethod


class Timeable(ABC):
    @abstractmethod
    def allow_passes_per_second(self, passes):
        pass

    def blocking_wait_seconds(self, seconds):
        pass