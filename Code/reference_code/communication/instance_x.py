from time import sleep

from sender import Sender
from resiver import Resiver


class Instance_X():
    
    def __init__(self, name) -> None:
        self.name = name
        self.active = False
        self.sender = Sender()
        self.resiver = Resiver()


    def run(self):
        for i in range(2):
            self.idle()
            self.act()
        print(f"Instance - {self.name} ends run")


    def act(self):
        print(f"Instance - {self.name} is aktiv")
        print(f"Instance - {self.name} reacts to {self.resiver.info}")


    def idle(self):
        self.active = False
        x = 0
        while not self.active and x < 5:
            x += 1
            print(f"Instance - {self.name} is idleing")
            sleep(3)
            if self.resiver.event_reseved:
                self.active = True
        

    def send(self, message = None):
        print(f"Instance - {self.name} sends message")
        if message != None:
            self.sender.set_event(name=message['name'], info=message['info'])
        else:
            self.sender.set_event(name='Ping', info='Hallo')
        self.sender.send()
