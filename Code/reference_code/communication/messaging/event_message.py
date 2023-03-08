from messaging import Distributor

class Event(Distributor): 
  
    
    def __init__(self, name =''): 
        Distributor.__init__(self) 
        self._name = name 
        self._information = "no event"
  
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def information(self): 
        return self._information 
  
    @information.setter 
    def information(self, value): 
        self._information = value
    
    def send(self):
        self.message_to_observers()