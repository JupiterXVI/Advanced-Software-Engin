from messaging import Event

class Sender():
    def __init__(self):
        self.e_message = Event(name="init message")

    def set_event(self, name, info):
        self.e_message.name = name
        self.e_message.information = info

    def add_listener(self, listener):
        self.e_message.attach_to_event(listener)

    def send(self):
        self.e_message.send()