from messaging import Listener

class Resiver(Listener):
    def __init__(self) -> None:
        self.event_reseved = False
        self._info = ""

    @property
    def info(self):
        self.event_reseved = False
        return self._info
    
    @info.setter
    def info(self, value):
        self._info = value

    def listen(self, send_event):
        print(f'event: {send_event.name} has been reseved')
        self.event_reseved = True
        self.info = send_event.information
