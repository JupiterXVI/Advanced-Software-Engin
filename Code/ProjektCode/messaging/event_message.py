from messaging import Distributor

class Event(Distributor): 
  
    
    def __init__(self, name =''): 
        Distributor.__init__(self) 
        self.name = name 
        self._data = 0
  
    @property
    def data(self): 
        return self._data 
  
    @data.setter 
    def data(self, value): 
        self._data = value 
        self.message() 