"""
imports
"""
from .distributer import Distributor


class Event(Distributor): 
    """
    global variables
    """
    def __init__(self, category =''): 
        Distributor.__init__(self) 
        self._category = category
        self._name = 'no event' 
        self._info = "no event"


    """
    functions
    """
    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, value):
        self._category = value
  

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        self._name = value


    @property
    def info(self): 
        return self._info


    @info.setter 
    def info(self, info): 
        self._info = info

    
    def send(self):
        self.message_to_observers()
