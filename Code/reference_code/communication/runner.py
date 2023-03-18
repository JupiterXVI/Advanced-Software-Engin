from communication import Sender, Resiver

class Runner():
    def __init__(self):
        self.sender = Sender()
        self.resiver = Resiver()
        self.run_forever = True
        self.funktion_with_parameters = ['myprint','add']


    def myprint(self, message):
        print(f"myPrint: {message} ")

    def byebye(self):
        print("bybye funktion")



    def run(self):
        while self.run_forever:
            if self.resiver.event_reseved:
                self.react_to_message(self.resiver.info)
            
    def react_to_message(self, request):
        if request["function"] in self.funktion_with_parameters:
            eval(f"self.{request['function']}")(request['parameter'])
        else:
            eval(f"self.{request['function']}")()

   