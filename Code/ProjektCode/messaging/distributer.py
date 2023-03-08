class Distributor: 
  
    
    def __init__(self): 
        self.observers = [] 
  

    def message(self, modifier = None): 
        for observer in self.observers: 
            if modifier != observer: 
                observer.listen(self) 
  

    def attach(self, observer): 
        if observer not in self.observers: 
            self.observers.append(observer) 
  
  
    def detach(self, observer): 
        try: 
            self.observers.remove(observer) 
        except ValueError: 
            pass