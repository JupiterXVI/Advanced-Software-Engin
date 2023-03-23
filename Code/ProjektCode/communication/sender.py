from communication import Event

class Sender():
    def __init__(self):
        self.e_message = Event(category="init")

    def set_event(self, category, name, info):
        self.e_message.category = category
        self.e_message.name = name
        self.e_message.info = info

    def add_listener(self, listener):
        self.e_message.attach_to_event(listener)

    def send(self):
        self.e_message.send()
