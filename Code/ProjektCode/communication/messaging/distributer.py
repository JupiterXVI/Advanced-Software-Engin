"""
imports
"""


class Distributor: 
    """
    global variables
    """
    def __init__(self): 
        self.observers = [] 
  

    """
    functions
    """
    def message_to_observers(self, modifier = None): 
        for observer in self.observers: 
            if modifier != observer: 
                observer.listen(self) 
  

    def attach_to_event(self, observer): 
        if observer not in self.observers: 
            self.observers.append(observer) 
  
  
    def detach_from_event(self, observer): 
        try: 
            self.observers.remove(observer) 
        except ValueError: 
            pass
        