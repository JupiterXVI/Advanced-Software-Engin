"""
imports
"""
from communication import Listener


class Reseiver(Listener):
    """
    global variables
    """
    def __init__(self) -> None:
        self._event_reseved = False
        self.message_queue = []


    """
    functions
    """
    @property
    def event_reseved(self):
        if len(self.message_queue) == 0:
            self._event_reseved = False
        else:    
            self._event_reseved = True
        return self._event_reseved
        

    def listen(self, send_event):
        self.message_queue.append({'category':send_event.category, 'name': send_event.name, 'info': send_event.info})


    def get_message(self):
        return self.message_queue.pop(0)
    

    def empty_message_queue(self):
        self.message_queue = []
    